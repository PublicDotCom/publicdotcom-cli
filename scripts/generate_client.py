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
    text = re.sub(r"^(\s*)'\*/\*':", r"\1application/json:", text, flags=re.MULTILINE)
    return _inject_enum_varnames(text)


def _enum_collision_key(value: str) -> str:
    """Approximate the enum member key openapi-python-client derives from a value."""
    return "_".join(re.findall(r"[A-Za-z0-9]+", value)).upper()


def _enum_varname(value: str, index: int) -> str:
    """Build a distinct, valid enum member name for a value like `AA+` or `SP-1`."""
    name = value.strip().upper()
    if not name or not name[0].isalpha():
        return f"VALUE_{index}"
    name = name.replace("+", "_PLUS")
    if name.endswith("-"):
        name = f"{name[:-1]}_MINUS"
    return re.sub(r"[^A-Z0-9]+", "_", name).strip("_")


def _inject_enum_varnames(text: str) -> str:
    """Add `x-enum-varnames` to enum blocks whose values collide after sanitization.

    openapi-python-client derives enum member names by stripping symbols, so values
    such as `AA+`, `AA`, and `AA-` (S&P bond ratings) all map to `AA` and generation
    fails with a duplicate-key error. Providing explicit `x-enum-varnames` keeps the
    enum values faithful to the spec while giving each member a distinct name.
    """
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    enum_re = re.compile(r"^(\s*)enum:\s*$")
    while i < len(lines):
        out.append(lines[i])
        match = enum_re.match(lines[i])
        if not match:
            i += 1
            continue
        indent = match.group(1)
        item_re = re.compile(rf"^({re.escape(indent)}\s+)- (\S.*?)\s*$")
        values: list[str] = []
        item_indent = ""
        j = i + 1
        while j < len(lines):
            item = item_re.match(lines[j])
            if not item:
                break
            item_indent = item.group(1)
            values.append(item.group(2).strip("'\""))
            out.append(lines[j])
            j += 1
        keys = [_enum_collision_key(value) for value in values]
        if values and len(set(keys)) != len(keys):
            varnames = [_enum_varname(value, index) for index, value in enumerate(values)]
            if len(set(varnames)) != len(varnames):
                raise SystemExit(f"Could not build distinct x-enum-varnames for enum: {values}")
            out.append(f"{indent}x-enum-varnames:")
            out.extend(f"{item_indent}- {varname}" for varname in varnames)
        i = j
    return "\n".join(out)


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
