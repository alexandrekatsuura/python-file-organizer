import pytest
import os
import shutil
from datetime import datetime
from unittest.mock import patch, MagicMock

from src.file_organizer import FileOrganizer

@pytest.fixture
def setup_organizer():
    source_dir = "/tmp/source_test"
    destination_dir = "/tmp/destination_test"
    
    # Ensure directories are clean before each test
    if os.path.exists(source_dir):
        shutil.rmtree(source_dir)
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)

    os.makedirs(source_dir)
    os.makedirs(destination_dir)

    organizer = FileOrganizer(source_dir, destination_dir)
    yield organizer

    # Clean up after tests
    if os.path.exists(source_dir):
        shutil.rmtree(source_dir)
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)

class TestFileOrganizer:

    def test_get_file_extension(self, setup_organizer):
        organizer = setup_organizer
        assert organizer._get_file_extension("document.pdf") == "pdf"
        assert organizer._get_file_extension("image.JPG") == "jpg"
        assert organizer._get_file_extension("archive.tar.gz") == "gz"
        assert organizer._get_file_extension("noextensionfile") == "no_extension"
        assert organizer._get_file_extension(".bashrc") == "bashrc"

    @patch("os.path.getctime")
    def test_get_creation_date(self, mock_getctime, setup_organizer):
        organizer = setup_organizer
        # Mock a specific timestamp (e.g., 2023-01-15)
        mock_getctime.return_value = datetime(2023, 1, 15, 10, 30, 0).timestamp()
        assert organizer._get_creation_date("/path/to/file.txt") == "2023-01-15"

    @patch("os.makedirs")
    @patch("shutil.move")
    @patch("os.path.isfile", return_value=True)
    @patch("os.listdir", return_value=["file1.txt", "image.png", "document.pdf"])
    def test_organize_by_type(self, mock_listdir, mock_isfile, mock_move, mock_makedirs, setup_organizer):
        organizer = setup_organizer
        organizer.organize_by_type()

        # Assert that os.makedirs was called for each extension
        mock_makedirs.assert_any_call(os.path.join(organizer.destination_directory, "txt"))
        mock_makedirs.assert_any_call(os.path.join(organizer.destination_directory, "png"))
        mock_makedirs.assert_any_call(os.path.join(organizer.destination_directory, "pdf"))

        # Assert that shutil.move was called for each file with correct paths
        mock_move.assert_any_call(os.path.join(organizer.source_directory, "file1.txt"), os.path.join(organizer.destination_directory, "txt", "file1.txt"))
        mock_move.assert_any_call(os.path.join(organizer.source_directory, "image.png"), os.path.join(organizer.destination_directory, "png", "image.png"))
        mock_move.assert_any_call(os.path.join(organizer.source_directory, "document.pdf"), os.path.join(organizer.destination_directory, "pdf", "document.pdf"))

        assert mock_move.call_count == 3

    @patch("os.makedirs")
    @patch("shutil.move")
    @patch("os.path.isfile", return_value=True)
    @patch("os.path.getctime")
    @patch("os.listdir")
    def test_organize_by_date(self, mock_listdir, mock_getctime, mock_isfile, mock_move, mock_makedirs, setup_organizer):
        organizer = setup_organizer

        # Mock os.listdir to return a list of files
        mock_listdir.return_value = ["file_a.txt", "file_b.jpg"]

        # Mock os.path.getctime to return different creation dates for files
        def mock_ctime_side_effect(filepath):
            if "file_a.txt" in filepath:
                return datetime(2024, 5, 10).timestamp()
            elif "file_b.jpg" in filepath:
                return datetime(2024, 5, 12).timestamp()
            return 0

        mock_getctime.side_effect = mock_ctime_side_effect

        organizer.organize_by_date()

        # Assert that os.makedirs was called for each date
        mock_makedirs.assert_any_call(os.path.join(organizer.destination_directory, "2024-05-10"))
        mock_makedirs.assert_any_call(os.path.join(organizer.destination_directory, "2024-05-12"))

        # Assert that shutil.move was called for each file with correct paths
        mock_move.assert_any_call(os.path.join(organizer.source_directory, "file_a.txt"), os.path.join(organizer.destination_directory, "2024-05-10", "file_a.txt"))
        mock_move.assert_any_call(os.path.join(organizer.source_directory, "file_b.jpg"), os.path.join(organizer.destination_directory, "2024-05-12", "file_b.jpg"))

        assert mock_move.call_count == 2