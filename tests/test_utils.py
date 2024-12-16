import sys
import os
import pytest

# Ustawienie ścieżki do modułów
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from python.utils import count_files_in_directory

def test_count_files_in_directory(tmpdir):
    """Test the count_files_in_directory function."""
    # Tworzenie tymczasowej struktury katalogów
    subdir = tmpdir.mkdir("subdir")
    subdir.join("file1.txt").write("content")
    subdir.join("file2.txt").write("content")

    subdir2 = tmpdir.mkdir("subdir2")
    subdir2.join("file3.txt").write("content")
    
    # Sprawdzenie liczby plików
    assert count_files_in_directory(str(tmpdir)) == 3
