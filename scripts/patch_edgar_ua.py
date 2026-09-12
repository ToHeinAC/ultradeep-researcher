#!/usr/bin/env python3
"""Re-apply the SEC EDGAR User-Agent patch to the installed hyperresearch.

The SEC's WAF rejects any request whose User-Agent contains a URL. hyperresearch
builds its UA from a hardcoded module constant that embeds the project's GitHub
URL, so every EDGAR request returns HTTP 403. The failure is silent: the
provider reports `available: True` (it only checks that a contact email is set)
and returns zero results with no error.

There is no environment variable or config key for the UA, so the constant has
to be rewritten in place. That edit lives in .venv, which is not tracked, so any
reinstall or upgrade of the package silently reverts it.

Run this after any environment change:

    uv run python scripts/patch_edgar_ua.py

Idempotent. Exits 0 if already patched, 1 if the target could not be patched.
See docs/edgar-ua-patch.md for the full diagnosis.
"""

from __future__ import annotations

import sys
from pathlib import Path

OLD = '_UA = "hyperresearch (https://github.com/jordan-gibbs/hyperresearch)"'
NEW = '_UA = "hyperresearch"'


def main() -> int:
    try:
        import hyperresearch
    except ImportError:
        print("hyperresearch is not installed in this environment", file=sys.stderr)
        return 1

    target = Path(hyperresearch.__file__).parent / "scholar" / "base.py"
    if not target.is_file():
        print(f"expected file not found: {target}", file=sys.stderr)
        return 1

    source = target.read_text(encoding="utf-8")

    if NEW in source and OLD not in source:
        print(f"already patched: {target}")
        return 0

    if OLD not in source:
        print(
            f"patch target not found in {target}\n"
            "The upstream constant has changed — re-diagnose before assuming "
            "EDGAR works. See docs/edgar-ua-patch.md.",
            file=sys.stderr,
        )
        return 1

    target.write_text(source.replace(OLD, NEW), encoding="utf-8")
    print(f"patched: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
