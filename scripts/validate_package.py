#!/usr/bin/env python3
"""Validate this single-server Cursor package without contacting services."""

import json
from pathlib import Path
import re
import struct

ROOT = Path(__file__).resolve().parent.parent


def contained_file(relative_path):
    path = Path(relative_path)
    assert not path.is_absolute() and ".." not in path.parts, f"Unsafe path: {path}"
    resolved = (ROOT / path).resolve()
    assert resolved.is_relative_to(ROOT) and resolved.is_file(), f"Missing/unsafe file: {path}"
    return resolved


def main():
    manifest = json.loads(contained_file(".cursor-plugin/plugin.json").read_text())
    assert manifest["name"] == "outfield"
    assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "Version must use semantic versioning"
    assert manifest["description"].strip()
    assert manifest["author"]["name"] == "Outfield"
    assert manifest["license"] == "MIT"
    assert manifest["repository"] == "https://github.com/outfieldco/outfield-plugin"
    assert manifest["homepage"] == "https://run.outfieldapp.com/docs/mcp"
    config = json.loads(contained_file(manifest["mcpServers"]).read_text())
    assert config == {"mcpServers": {"outfield": {"url": "https://run.outfieldapp.com/mcp"}}}, \
        "The package must contain exactly one hosted connection, without auth overrides or credentials"
    logo = contained_file(manifest["logo"]).read_bytes()
    assert logo[:8] == b"\x89PNG\r\n\x1a\n", "Logo must be a PNG"
    width, height = struct.unpack(">II", logo[16:24])
    assert width >= 256 and height >= 256 and len(logo) <= 5 * 1024 * 1024
    for name in ("README.md", "LICENSE"):
        contained_file(name)
    allowed = {
        ".cursor-plugin/plugin.json", "mcp.json", "assets/logo.png", "README.md",
        "LICENSE", "scripts/validate_package.py", ".gitignore"
    }
    files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.relative_to(ROOT).parts]
    assert all(p.relative_to(ROOT).as_posix() in allowed for p in files), "Unexpected packaged file"
    for path in files:
        assert not path.is_symlink(), f"Do not package symlinks: {path.name}"
        if path.suffix == ".png":
            continue
        content = path.read_text()
        assert not re.search(r"(?:sk-proj-|gh[opusr]_)[A-Za-z0-9_-]{20,}", content), \
            f"Possible credential in {path.name}"
        private_key_header = "-----BEGIN " + "PRIVATE KEY-----"
        assert private_key_header not in content, f"Private key in {path.name}"
    print(f"Package valid: {manifest['name']} {manifest['version']}; one remote OAuth MCP; logo {width}x{height}")


if __name__ == "__main__":
    main()
