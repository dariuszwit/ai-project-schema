## Release v1.0.4 - September 19, 2025

### Added
- Initial release of AI Project Schema extension for VS Code.
- Automatically creates `.ai-schema-ignore` file if it doesn't exist (no overwrite).
- Default keybinding `Ctrl+Alt+G` (Windows/Linux) or `Cmd+Alt+G` (macOS) for "Generate Project Schema".

### Changed
- Removed generation of `schema-full.txt` to improve performance.
- Updated command names to "AI Project Schema: Generate Project Schema" for consistency.

### Fixed
- Resolved import errors in Python scripts (`main.py`, `structure.py`).
- Ensured all required files (`main.py`, `paths.py`, `structure.py`, `ignore.py`) are included in the .vsix package.