# news-image-20261117: one image that sums up 17 November 2026
#
# A make.fun entry (Python 3.13, standard library only). The image the
# program writes is the entry.png beside this file: a newspaper front
# page drawn for Tuesday 17 November 2026, with the day's six biggest
# stories and a ticker of four more. The program copies it to
# /output/entry.png, so both graded runs write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import struct
import sys

# The gate takes a whole PNG of at most 1 MiB and 1024 by 1024 pixels.
MAX_BYTES = 1048576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def read_png_size(path):
    """Return (width, height) from a PNG header, or None if not a PNG."""
    with open(path, "rb") as handle:
        head = handle.read(33)
    if len(head) < 33 or head[:8] != PNG_MAGIC:
        return None
    # After the 8-byte magic comes the 25-byte IHDR chunk: length (4),
    # type "IHDR" (4), width (4, big-endian), height (4, big-endian).
    if head[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    # In the grader's container the output directory is /output; outside
    # it, MAKEFUN_OUTPUT_DIR stands in for it (see the header comment).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    size = read_png_size(source)
    if size is None:
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    width, height = size
    if width > MAX_SIDE or height > MAX_SIDE:
        print("entry.png is %dx%d, over 1024x1024" % (width, height),
              file=sys.stderr)
        return 1
    if os.path.getsize(source) > MAX_BYTES:
        print("entry.png is over 1 MiB", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, target)
    print("wrote %s (%dx%d)" % (target, width, height))
    return 0


if __name__ == "__main__":
    sys.exit(main())
