#!/usr/bin/env python3
"""One Word, One Username, One Reward -- entry writer.

Writes the account owner's own make.fun handle (exactly one word,
no spaces, no explanation) to entry.txt inside MAKEFUN_OUTPUT_DIR.
Standard library only, no network access, fully deterministic.
"""

import os
import stat
from pathlib import Path

# Handle built from its parts: family name + given name, joined by "-".
_FAMILY = "saputra"
_GIVEN = "ady"
_HANDLE = _FAMILY + "-" + _GIVEN


def main() -> int:
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    if not 1 <= len(_HANDLE) <= 30:
        raise SystemExit("handle length out of range (must be 1-30 chars)")
    if any(ch.isspace() for ch in _HANDLE):
        raise SystemExit("handle must be a single word without spaces")
    data = _HANDLE.encode("utf-8")
    target.write_bytes(data)
    os.chmod(target, 0o644)
    # Read back and verify exactly what was written.
    if target.read_bytes() != data:
        raise SystemExit("read-back mismatch")
    if stat.S_IMODE(target.stat().st_mode) != 0o644:
        raise SystemExit("unexpected file mode")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
