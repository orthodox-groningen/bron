#!/usr/bin/env python3
"""Patch site_url and preview flag in mkdocs.yml for CI builds."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <site_url> <preview:true|false>", file=sys.stderr)
        return 2

    site_url = sys.argv[1].rstrip("/") + "/"
    preview = sys.argv[2].lower() in {"1", "true", "yes"}

    path = Path("mkdocs.yml")
    text = path.read_text(encoding="utf-8")
    text, n_url = re.subn(
        r"^site_url:\s*.+$",
        f"site_url: {site_url}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if n_url != 1:
        print("Could not patch site_url in mkdocs.yml", file=sys.stderr)
        return 1

    text, n_preview = re.subn(
        r"^  preview:\s*.+$",
        f"  preview: {str(preview).lower()}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if n_preview != 1:
        print("Could not patch extra.preview in mkdocs.yml", file=sys.stderr)
        return 1

    path.write_text(text, encoding="utf-8")
    print(f"site_url={site_url} preview={preview}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
