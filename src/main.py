from file_organizer import FileOrganizer
import os

class Main:
    """
    The main entry point for the file organizer application.
    This class handles user interaction and orchestrates the file organization process.
    """

    def __init__(self):
        """
        Initializes the Main class.
        """
        self._organizer = None

    def _get_user_input(self):
        """
        Prompts the user for the source and destination directories.

        Returns:
            tuple: A tuple containing the source and destination directory paths.
        """
        source_dir = input("Enter the source directory path to organize: ")
        dest_dir = input("Enter the destination directory path: ")
        return source_dir, dest_dir

    def run(self):
        """
        Executes the main application loop.
        """
        print("\n--- File Organizer ---")
        
        source, destination = self._get_user_input()

        if not os.path.isdir(source):
            print(f"Error: Source directory \'{source}\' does not exist.")
            return

        self._organizer = FileOrganizer(source, destination)

        while True:
            print("\nChoose an organization method:")
            print("1. Organize by file type/extension")
            print("2. Organize by creation date")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                self._organizer.organize_by_type()
                break
            elif choice == '2':
                self._organizer.organize_by_date()
                break
            elif choice == '3':
                print("Exiting.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main = Main()
    main.run()


