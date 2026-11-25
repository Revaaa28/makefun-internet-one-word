#!/usr/bin/env python3
"""Entry point: write the one word that sums up the internet to /output/entry.txt."""

import os


def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("feral")


if __name__ == "__main__":
    main()
