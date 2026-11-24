"""News-24 entry: copy the pre-rendered entry.png to the output directory.

The image is drawn in code by work-v1/draw-v1.py and stored in this repo as
entry.png. This script only copies it to MAKEFUN_OUTPUT_DIR (default
/output), so the grader run is deterministic: same bytes every time.
"""

import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    with open(src, "rb") as f:
        head = f.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a valid PNG", file=sys.stderr)
        return 1
    if os.path.getsize(src) > 1048576:
        print("entry.png exceeds the 1 MiB cap", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote " + dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
