import os
import fnmatch

def load_ignore_list(ignore_file_path):
    """Load ignore patterns from .ai-schema-ignore file (supports # comments)."""
    patterns = []
    if os.path.exists(ignore_file_path):
        with open(ignore_file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith('#'):
                    continue
                patterns.append(line)
        # print(f"[INFO] Loaded ignore file: {ignore_file_path} ({len(patterns)} patterns)")  # Wyłączone
    else:
        # print(f"[WARN] Ignore file not found: {ignore_file_path}")  # Wyłączone
        pass
    return patterns

def _normalize_pattern(pat: str) -> str:
    """Normalize pattern for OS paths (slashes)."""
    pat = pat.strip('\'"')
    if pat.startswith("./"):
        pat = pat[2:]
    return pat.replace("/", os.sep)

def is_ignored(path: str, ignore_list: list[str], project_root: str | None = None) -> bool:
    """Check if path should be ignored."""
    if not ignore_list:
        # print(f"[CHECK] {path} -> no patterns loaded")  # Wyłączone
        return False

    norm_path = os.path.normpath(path)
    rel_path = norm_path
    if project_root:
        try:
            rel_path = os.path.relpath(norm_path, project_root)
        except Exception:
            rel_path = norm_path
    rel_path = os.path.normpath(rel_path)
    base_name = os.path.basename(norm_path)

    # print(f"[CHECK] Checking path: {rel_path} (basename={base_name})")  # Wyłączone

    for raw_pat in ignore_list:
        pat = _normalize_pattern(raw_pat)
        if not pat:
            continue

        # Strip trailing separator only for fnmatch comparisons
        stripped_pat = pat.rstrip(os.sep)

        # Basename match (for files or directories)
        if fnmatch.fnmatch(base_name, stripped_pat):
            # print(f"[IGNORED] {rel_path} (matched basename {pat})")  # Wyłączone
            return True

        # Relative path match (for files or directories)
        if fnmatch.fnmatch(rel_path, stripped_pat):
            # print(f"[IGNORED] {rel_path} (matched relpath {pat})")  # Wyłączone
            return True

        # Directory prefix match (for recursive directory ignores)
        if rel_path == stripped_pat or rel_path.startswith(stripped_pat + os.sep):
            # print(f"[IGNORED] {rel_path} (matched dir prefix {pat})")  # Wyłączone
            return True

        # Full path match (fallback)
        if fnmatch.fnmatch(norm_path, stripped_pat):
            # print(f"[IGNORED] {rel_path} (matched full path {pat})")  # Wyłączone
            return True

        # Exact directory match with trailing separator
        if pat.endswith(os.sep) and (rel_path + os.sep) == pat:
            # print(f"[IGNORED] {rel_path} (matched exact dir {pat})")  # Wyłączone
            return True

    # print(f"[NOT IGNORED] {rel_path}")  # Wyłączone
    return False