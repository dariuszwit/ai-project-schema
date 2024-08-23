import os

def generate_full_tree_structure(root_dir, output_lines, level=0):
    """Generuje pełną strukturę drzewa projektu, bez względu na zignorowane pliki."""
    try:
        for item in sorted(os.listdir(root_dir)):
            item_path = os.path.join(root_dir, item)
            output_lines.append(" " * level * 4 + "|-- " + item)
            if os.path.isdir(item_path):
                generate_full_tree_structure(item_path, output_lines, level + 1)
    except Exception as e:
        output_lines.append(f"Błąd podczas przetwarzania {root_dir}: {str(e)}")
