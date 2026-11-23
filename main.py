"""把本仓库的 entry.png 原样送到输出目录。

不做裁剪、不做转码、不做重命名：读进来多少字节，
写出去就是多少字节。行为完全确定，与时间、网络、
随机数一概无关。
"""

import os
import sys


def source_file():
    """entry.png 与本文件同在仓库根目录。"""
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, "entry.png")


def output_folder():
    """输出目录由环境变量指定，缺省为 /output。"""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not chosen:
        chosen = "/output"
    return chosen


def move_bytes(origin, destination):
    """一块一块地读，再一块一块地写，不改动任何字节。"""
    with open(origin, "rb") as incoming:
        with open(destination, "wb") as outgoing:
            while True:
                piece = incoming.read(8192)
                if not piece:
                    break
                outgoing.write(piece)


def main():
    origin = source_file()
    folder = output_folder()
    os.makedirs(folder, exist_ok=True)
    destination = os.path.join(folder, "entry.png")
    move_bytes(origin, destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
