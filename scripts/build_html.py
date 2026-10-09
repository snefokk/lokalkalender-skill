#!/usr/bin/env python3
"""Bygger den selvstendige HTML-kalenderen fra en config-fil + malen.

Kun standardbiblioteket — ingen pip install.

    python3 scripts/build_html.py \
        --config arbeid/config.json \
        --template templates/kalender-mal.html \
        --output outputs/hva-skjer-i-roros.html
"""
import argparse
import base64
import json
import re
import sys
from pathlib import Path

DEFAULT_FARGER = {
    "bg": "#faf8f4",
    "ink": "#1a1a1a",
    "ink_soft": "#4a4a4a",
    "accent": "#3d1f4d",
    "rule": "rgba(26, 26, 26, 0.12)",
}

DEFAULT_FONTER = {
    "overskrift": "Newsreader",
    "brodtekst": "Inter",
}
DEFAULT_FONT_URL = (
    "https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;"
    "0,6..72,700;1,6..72,400;1,6..72,500&family=Inter:wght@400;500;600&display=swap"
)
SERIF_FALLBACK = "Georgia, 'Times New Roman', serif"
SANS_FALLBACK = "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
FONT_NAME_RE = re.compile(r"^[A-Za-z0-9 \-]+$")


def font_setup(fonter: dict) -> dict:
    """Bygger CSS-verdier og Google Fonts-URL fra config['fonter'].

    Uten egne fonter brukes Snefokk-standarden (Newsreader + Inter).
    """
    if not fonter:
        return {
            "{{FONT_URL}}": DEFAULT_FONT_URL,
            "{{FONT_HEADING}}": f"'Newsreader', {SERIF_FALLBACK}",
            "{{FONT_BODY}}": f"'Inter', {SANS_FALLBACK}",
        }

    overskrift = fonter.get("overskrift", DEFAULT_FONTER["overskrift"])
    brodtekst = fonter.get("brodtekst", DEFAULT_FONTER["brodtekst"])
    for navn in (overskrift, brodtekst):
        if not FONT_NAME_RE.match(navn):
            raise ValueError(f"Ugyldig fontnavn: {navn!r} (bare bokstaver, tall, mellomrom og bindestrek)")

    url = fonter.get("google_fonts_url")
    if not url:
        fam = lambda n: "family=" + n.replace(" ", "+") + ":wght@400;500;600;700"
        url = "https://fonts.googleapis.com/css2?" + "&".join(sorted({fam(overskrift), fam(brodtekst)})) + "&display=swap"

    return {
        "{{FONT_URL}}": url,
        "{{FONT_HEADING}}": f"'{overskrift}', {SANS_FALLBACK}",
        "{{FONT_BODY}}": f"'{brodtekst}', {SANS_FALLBACK}",
    }


LOGO_PATH = Path(__file__).resolve().parent.parent / "templates" / "assets" / "snefokk-logo.png"


def snefokk_logo_data_uri() -> str:
    data = LOGO_PATH.read_bytes()
    return "data:image/png;base64," + base64.b64encode(data).decode("ascii")


def build(config: dict, template: str) -> str:
    farger = {**DEFAULT_FARGER, **config.get("farger", {})}
    arrangementer = config.get("arrangementer", [])

    data_json = json.dumps(
        {
            "arrangementer": arrangementer,
            "skjul_passerte": config.get("skjul_passerte", True),
        },
        ensure_ascii=False,
    )
    # Unngå at "</script>" i data (f.eks. i en tittel) bryter ut av script-taggen.
    data_json = data_json.replace("</", "<\\/")

    kilde_note = config.get("kilde_note", "")

    replacements = {
        "{{TITLE}}": config.get("tittel", "Aktivitetskalender"),
        "{{EYEBROW}}": config.get("eyebrow", "Aktivitetskalender"),
        "{{H1}}": config.get("h1", "Hva skjer"),
        "{{SUBTITLE}}": config.get("undertittel", ""),
        "{{GENERATED}}": config.get("generert", ""),
        "{{SOURCE_NOTE}}": kilde_note,
        "{{COLOPHON}}": config.get("colophon", ""),
        "{{BG}}": farger["bg"],
        "{{INK}}": farger["ink"],
        "{{INK_SOFT}}": farger["ink_soft"],
        "{{HEADING}}": farger.get("heading", farger["ink"]),
        "{{HEADING_WEIGHT}}": str(int(config.get("fonter", {}).get("overskrift_vekt", 500))),
        "{{ACCENT}}": farger["accent"],
        "{{RULE}}": farger["rule"],
        "{{DATA_JSON}}": data_json,
        "{{SNEFOKK_LOGO}}": snefokk_logo_data_uri(),
        **font_setup(config.get("fonter", {})),
    }

    html = template
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)
    return html


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--template", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    template = args.template.read_text(encoding="utf-8")

    html = build(config, template)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")

    n = len(config.get("arrangementer", []))
    print(f"Skrev {args.output} ({n} arrangementer).")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"Fant ikke fil: {e.filename}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Ugyldig JSON i config-fila: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
