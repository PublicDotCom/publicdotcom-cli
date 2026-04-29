from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "spec.yaml"
OUTPUT_PATH = ROOT / "src" / "publicdotcom_cli" / "_generated"


def normalized_spec_text() -> str:
    if not SPEC_PATH.exists():
        raise SystemExit(
            f"OpenAPI spec not found at {SPEC_PATH}. "
            "Place the local, uncommitted spec at the repository root as spec.yaml."
        )
    text = SPEC_PATH.read_text(encoding="utf-8")
    return re.sub(r"^(\s*)'\*/\*':", r"\1application/json:", text, flags=re.MULTILINE)


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        normalized_spec = Path(tmp) / "spec.codegen.yaml"
        normalized_spec.write_text(normalized_spec_text(), encoding="utf-8")
        subprocess.run(
            [
                "uvx",
                "openapi-python-client",
                "generate",
                "--path",
                str(normalized_spec),
                "--output-path",
                str(OUTPUT_PATH),
                "--overwrite",
                "--meta",
                "none",
            ],
            check=True,
            cwd=ROOT,
        )

    shutil.rmtree(OUTPUT_PATH / ".ruff_cache", ignore_errors=True)


if __name__ == "__main__":
    main()
