import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from python.utils import count_files_in_directory

def test_count_files_in_directory(tmpdir):
    """Test the count_files_in_directory function."""
    # Tworzenie tymczasowej struktury katalogów
    tmpdir.mkdir("subdir").join("file1.txt").write("content")
    tmpdir.mkdir("subdir").join("file2.txt").write("content")
    tmpdir.mkdir("subdir2").join("file3.txt").write("content")
    
    # Sprawdzenie liczby plików
    assert count_files_in_directory(str(tmpdir)) == 3
