#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: Path) -> None:
    if not path.exists():
        raise SystemExit(f"missing required path: {path}")


def main() -> None:
    for name in ["README.md", "README.en.md", "README.git-flow.md", "CHANGELOG.md", "COURSE", "Makefile", "package.json", "template", "labs"]:
        require(ROOT / name)
    for number in range(1, 9):
        slug = f"lab{number:02d}"
        lab_dir = ROOT / "labs" / slug
        require(lab_dir)
        for rel in ["README.md", "INSTRUCTIONS.md", "CHANGELOG.md", "RELEASE.md", "project", "report", "presentation"]:
            require(lab_dir / rel)
        require(lab_dir / "project" / "src")
        require(lab_dir / "project" / "scripts")
        require(lab_dir / "project" / "docs")
        require(lab_dir / "project" / "test")
        require(lab_dir / "project" / "notebook")
        require(lab_dir / "project" / "markdown")
        require(lab_dir / "project" / "data")
        require(lab_dir / "project" / "plots")
        require(next((lab_dir / "report").glob("*.qmd")))
        require(next((lab_dir / "presentation").glob("*.qmd")))
        require(next((lab_dir / "report").glob("*.html")))
        require(next((lab_dir / "report").glob("*.docx")))
        require(next((lab_dir / "presentation").glob("*.html")))
        require(next((lab_dir / "presentation").glob("*.pptx")))
        subprocess.run(["julia", "--project=.", "test/runtests.jl"], check=True, cwd=lab_dir / "project")

    manifest = ROOT / "tools" / "generated" / "manifest.json"
    require(manifest)
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    if len(payload.get("labs", [])) != 8:
        raise SystemExit("manifest does not list eight labs")

    print("verification passed")


if __name__ == "__main__":
    main()
