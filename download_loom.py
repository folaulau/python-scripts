#!/usr/bin/env python3
"""Download Loom videos as MP4 files."""

import subprocess
import sys
import os


def download_loom(url: str, output_dir: str = None):
    if output_dir is None:
        output_dir = os.path.expanduser("~/Downloads")

    # Extract video ID from URL for filename
    video_id = url.rstrip("/").split("/")[-1].split("?")[0]
    output_path = os.path.join(output_dir, f"loom-{video_id}.mp4")

    cmd = [
        "yt-dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "--merge-output-format", "mp4",
        "-o", output_path,
        url,
    ]

    print(f"Downloading: {url}")
    print(f"Saving to:   {output_path}")
    result = subprocess.run(cmd)

    if result.returncode == 0:
        print(f"\nDone! Saved to {output_path}")
    else:
        print("\nDownload failed.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <loom-url> [output-dir]")
        sys.exit(1)

    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    download_loom(url, output_dir)
