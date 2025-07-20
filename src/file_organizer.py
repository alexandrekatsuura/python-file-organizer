
import os
import shutil
from datetime import datetime

class FileOrganizer:
    """
    A class to organize files in a given directory based on their type/extension
    and creation date.
    """

    def __init__(self, source_directory: str, destination_directory: str):
        """
        Initializes the FileOrganizer with source and destination directories.

        Args:
            source_directory (str): The path to the directory containing files to be organized.
            destination_directory (str): The path to the directory where organized files will be moved.
        """
        self.source_directory = source_directory
        self.destination_directory = destination_directory

        if not os.path.exists(self.destination_directory):
            os.makedirs(self.destination_directory)

    def _get_file_extension(self, filename: str) -> str:
        """
        Extracts the file extension from a given filename.

        Args:
            filename (str): The name of the file.

        Returns:
            str: The file extension (e.g., 'txt', 'pdf', 'jpg').
        """
        return filename.split('.')[-1].lower() if '.' in filename else 'no_extension'

    def _get_creation_date(self, filepath: str) -> str:
        """
        Gets the creation date of a file in YYYY-MM-DD format.

        Args:
            filepath (str): The full path to the file.

        Returns:
            str: The creation date as a string (YYYY-MM-DD).
        """
        timestamp = os.path.getctime(filepath)
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

    def organize_by_type(self):
        """
        Organizes files in the source directory into subdirectories based on their file type/extension.
        """
        print(f"\nOrganizing files by type in: {self.source_directory}")
        for filename in os.listdir(self.source_directory):
            source_filepath = os.path.join(self.source_directory, filename)
            if os.path.isfile(source_filepath):
                extension = self._get_file_extension(filename)
                destination_path = os.path.join(self.destination_directory, extension)
                
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                
                shutil.move(source_filepath, os.path.join(destination_path, filename))
                print(f"Moved '{filename}' to '{extension}/'")

    def organize_by_date(self):
        """
        Organizes files in the source directory into subdirectories based on their creation date.
        """
        print(f"\nOrganizing files by creation date in: {self.source_directory}")
        for filename in os.listdir(self.source_directory):
            source_filepath = os.path.join(self.source_directory, filename)
            if os.path.isfile(source_filepath):
                creation_date = self._get_creation_date(source_filepath)
                destination_path = os.path.join(self.destination_directory, creation_date)
                
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                
                shutil.move(source_filepath, os.path.join(destination_path, filename))
                print(f"Moved '{filename}' to '{creation_date}/'")

