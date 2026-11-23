#!/usr/bin/env python3
"""Entry point: copy the pre-drawn front page to the grader's output path.

Deterministic by construction: the file is copied byte for byte, with no
network, no randomness and no time dependence. Standard library only.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
