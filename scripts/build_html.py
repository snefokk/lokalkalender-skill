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
import sys
from pathlib import Path

DEFAULT_FARGER = {
    "bg": "#faf8f4",
    "ink": "#1a1a1a",
    "ink_soft": "#4a4a4a",
    "accent": "#3d1f4d",
    "rule": "rgba(26, 26, 26, 0.12)",
}

LOGO_PATH = Path(__file__).resolve().parent.parent / "templates" / "assets" / "snefokk-logo.png"


def snefokk_logo_data_uri() -> str:
    data = LOGO_PATH.read_bytes()
    return "data:image/png;base64," + base64.b64encode(data).decode("ascii")


def build(config: dict, template: str) -> str:
    farger = {**DEFAULT_FARGER, **config.get("farger", {})}
    arrangementer = config.get("arrangementer", [])

    data_json = json.dumps({"arrangementer": arrangementer}, ensure_ascii=False)
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
        "{{ACCENT}}": farger["accent"],
        "{{RULE}}": farger["rule"],
        "{{DATA_JSON}}": data_json,
        "{{SNEFOKK_LOGO}}": snefokk_logo_data_uri(),
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
