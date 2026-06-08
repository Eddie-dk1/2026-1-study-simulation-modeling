#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def render_one(src: Path, dst: Path, extra: list[str] | None = None) -> None:
    cmd = ["pandoc", src.name, "-f", "markdown", "-o", dst.name]
    if extra:
        cmd.extend(extra)
    subprocess.run(cmd, check=True, cwd=src.parent)


def main() -> None:
    for lab_dir in sorted((ROOT / "labs").glob("lab*")):
        report = next((lab_dir / "report").glob("*.qmd"))
        presentation = next((lab_dir / "presentation").glob("*.qmd"))
        render_one(report, report.with_suffix(".html"), ["-s"])
        render_one(report, report.with_suffix(".docx"))
        render_one(presentation, presentation.with_suffix(".html"), ["-s"])
        render_one(presentation, presentation.with_suffix(".pptx"))


if __name__ == "__main__":
    main()
