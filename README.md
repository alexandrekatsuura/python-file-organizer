# 📁 File Organizer

![GitHub repo size](https://img.shields.io/github/repo-size/alexandrekatsuura/python-file-organizer?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alexandrekatsuura/python-file-organizer?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alexandrekatsuura/python-file-organizer?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/alexandrekatsuura/python-file-organizer?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/alexandrekatsuura/python-file-organizer?style=for-the-badge)

## ℹ️ About

This project is a command-line application built in Python designed to help users organize their files based on type/extension or creation date. It provides a simple yet effective way to declutter directories, making it easier to manage digital assets. The project emphasizes clean code, modular design, and includes unit tests to ensure reliability.

## 🚀 Features

*   **Organize by Type/Extension**: Automatically moves files into subdirectories named after their file extensions (e.g., `documents/`, `images/`, `videos/`).
*   **Organize by Creation Date**: Arranges files into subdirectories based on their creation date (e.g., `2023-01-15/`, `2023-02-28/`).
*   **Command-Line Interface (CLI)**: User-friendly interface for selecting organization methods and specifying directories.
*   **Error Handling**: Gracefully handles invalid directory paths.
*   **Unit Testing**: Comprehensive tests using `pytest` to ensure core functionalities work as expected.
*   **Clean Project Structure**: Follows a standard Python project layout for clarity and maintainability.

## 🛠️ Technologies Used

*   **Python 3.x**
*   **`pytest`**: Framework used for unit testing.

## ⚙️ How to Run the Project

### Prerequisites

Ensure that Python 3.x is installed on your machine.

### Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/alexandrekatsuura/python-file-organizer
    cd python-file-organizer
    ```

2.  (Optional but recommended) Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate      # On Linux/macOS
    # .venv\Scripts\activate       # On Windows
    ```

3.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

To run the program, use the following command:

```bash
python src/main.py
```

You will be prompted to enter the source directory (where your unorganized files are) and the destination directory (where you want the organized files to go). Then, you can choose your preferred organization method.

## ✅ Running the Tests

To run the unit tests, from the project root directory:

```bash
pytest -v
```

This will execute all test cases located in the `tests/` directory.

## 📁 Project Structure

```bash
python-file-organizer/
├── src/
│   ├── main.py             # Main application entry point and CLI logic
│   └── file_organizer.py   # Core logic for file organization
├── tests/
│   └── test_file_organizer.py # Unit tests for the FileOrganizer class
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).


