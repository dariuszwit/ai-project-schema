import os
from python.tree_structure import generate_filtered_tree_structure

def test_generate_filtered_tree_structure(tmpdir):
    # Tworzenie struktury katalogów
    test_dir = tmpdir.mkdir("test-dir")
    test_file = test_dir.join("file.txt")
    test_file.write("Sample content")
    ignore_list = ['*.log', '/node_modules/']

    # Test generowania struktury drzewa
    result = generate_filtered_tree_structure(str(tmpdir), ignore_list)
    assert len(result) > 0
    assert any("test-dir" in r[0] for r in result)
