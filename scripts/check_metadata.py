#!/usr/bin/env python3
"""Compare publication metadata copies; this does not validate scientific claims.

Standard library only. Supports this repository's Markdown version line, quoted
CFF title/version/date scalars and folded abstract, and Zenodo HTML paragraphs.
Unknown or missing source formats fail explicitly rather than skipping a field.
"""
from __future__ import annotations

import datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys


def one(pattern: str, text: str, label: str) -> str:
    matches = re.findall(pattern, text, re.MULTILINE)
    if len(matches) != 1:
        raise ValueError(f"{label}: expected exactly one supported field, found {len(matches)}")
    return matches[0]


def cff_scalar(text: str, key: str) -> str:
    value = one(rf"^{re.escape(key)}: (.+)$", text, f"CITATION.cff {key}")
    # These fields use JSON-compatible double-quoted YAML strings in this repo.
    parsed = json.loads(value)
    if not isinstance(parsed, str) or not parsed.strip():
        raise ValueError(f"CITATION.cff {key}: expected a nonempty quoted string")
    return parsed


class DescriptionText(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in {"p", "br", "div"}:
            self.parts.append(" ")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"p", "div"}:
            self.parts.append(" ")


def check(root: Path) -> None:
    paper = (root / "paper.md").read_text()
    cff = (root / "CITATION.cff").read_text()
    zenodo = json.loads((root / ".zenodo.json").read_text())
    version_line = one(r"^\*\*Version:\*\* ([^\n]+)$", paper, "paper.md version/date")
    match = re.match(r"([^,\s]+), (\d{4}-\d{2}-\d{2})(?:\.|\s|$)", version_line)
    if not match:
        raise ValueError("paper.md version/date: unsupported version line")
    version, date = match.groups()
    datetime.date.fromisoformat(date)
    reference = {
        "title": one(r"^# (.+)$", paper, "paper.md title"),
        "version": version,
        "date": date,
        "abstract": one(r"(?s)^## Abstract\n\n(.+?)\n\n\*\*Keywords:\*\*", paper, "paper.md abstract"),
    }
    # Only indented lines and blank lines belong to the folded CFF abstract.
    abstract = one(r"^abstract: >\n((?:[ \t]+[^\n]*\n|\n)+)", cff, "CITATION.cff abstract")
    cff_values = {key: cff_scalar(cff, key) for key in ("title", "version")}
    cff_values.update(date=cff_scalar(cff, "date-released"), abstract=abstract)
    description = zenodo.get("description")
    if not isinstance(description, str):
        raise ValueError(".zenodo.json description: expected HTML text")
    parser = DescriptionText()
    parser.feed(description)
    parser.close()
    zenodo_values = {key: zenodo.get(key) for key in ("title", "version")}
    zenodo_values.update(date=zenodo.get("publication_date"), abstract="".join(parser.parts))
    for source, values in (("CITATION.cff", cff_values), (".zenodo.json", zenodo_values)):
        for key, expected in reference.items():
            actual = values[key]
            if not isinstance(actual, str) or " ".join(actual.split()) != " ".join(expected.split()):
                raise ValueError(f"{source} {key} does not match paper.md")


def main() -> int:
    try:
        check(Path(__file__).resolve().parent.parent)
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print("Metadata matches: manuscript, CFF and Zenodo title/version/date/abstract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
