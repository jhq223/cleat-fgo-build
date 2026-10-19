"""Create the APK update manifest from the signed release artifact."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import quote


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apk", type=Path, default=Path("dist/fgo-mod.apk"))
    parser.add_argument("--version", required=True)
    parser.add_argument("--version-code", required=True, type=int)
    parser.add_argument("--module-version", required=True)
    parser.add_argument("--tag", help="Release tag; defaults to the game version")
    args = parser.parse_args()
    with args.apk.open("rb") as file:
        digest = hashlib.file_digest(file, "sha256").hexdigest()
    manifest = {
        "schema": 1,
        "version": args.version,
        "version_code": args.version_code,
        "module_version": args.module_version.lstrip("v"),
        "url": "https://github.com/jhq223/cleat-fgo-build/releases/download/"
        + quote(args.tag or args.version, safe="") + "/fgo-mod.apk",
        "size": args.apk.stat().st_size,
        "sha256": digest,
    }
    args.apk.with_name("update.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
