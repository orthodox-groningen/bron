"""Controleer of zangstuk.yaml overeenkomt met VSA-frontmatter."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

_VSA_SRC = Path(__file__).resolve().parents[2] / "VSA-tooling" / "src"
if _VSA_SRC.is_dir() and str(_VSA_SRC) not in sys.path:
    sys.path.insert(0, str(_VSA_SRC))

from vsa.yaml_frontmatter import parse_vsa_frontmatter  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--zangstukken-root",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "zangstukken",
    )
    args = parser.parse_args()
    errors: list[str] = []

    for zdir in sorted(args.zangstukken_root.iterdir()):
        if not zdir.is_dir():
            continue
        yaml_path = zdir / "zangstuk.yaml"
        vsa_path = zdir / "sources" / "vsa" / "groningen.vsa"
        if not yaml_path.is_file() or not vsa_path.is_file():
            continue

        data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        fm, _ = parse_vsa_frontmatter(vsa_path.read_text(encoding="utf-8"))
        ident = fm.get("identificatie") or {}

        checks = {
            "title": (data.get("title"), ident.get("title")),
            "tone": (data.get("tone"), ident.get("tone")),
        }
        for field, (yaml_val, fm_val) in checks.items():
            if yaml_val != fm_val:
                errors.append(f"{zdir.name}: {field} yaml={yaml_val!r} frontmatter={fm_val!r}")

        for src in data.get("sources") or []:
            if src.get("id") != "groningen":
                continue
            if src.get("reference") != ident.get("bron"):
                errors.append(f"{zdir.name}: reference mismatch")
            if src.get("composer") != ident.get("composer"):
                errors.append(f"{zdir.name}: composer mismatch")
            if src.get("language") != ident.get("language"):
                errors.append(f"{zdir.name}: language mismatch")

    if errors:
        print("Fouten:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("OK: alle VSA-zangstukken yaml in sync met frontmatter")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
