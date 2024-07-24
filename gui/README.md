# PDF to DOCX Converter GUI

This project provides a graphical user interface (GUI) for converting PDF files to DOCX format. The application is built using Tkinter and packaged into a standalone executable for easy distribution.

## Features

- **Convert PDF to DOCX:** Easily convert PDF files to DOCX format using a simple GUI.
- **Browse for Files:** Select PDF files using a file dialog.
- **Specify Output File:** Optionally set the name for the output DOCX file.
- **Error Handling:** Provides feedback on invalid files or conversion errors.

## Requirements

- Python 3.x
- `pdf2docx` library
- `tkinter` (included with Python standard library)
- PyInstaller (for packaging into an executable)

## Installation

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installing Dependencies

Install the required Python libraries using `pip`:

```bash
pip install pdf2docx
```

### Running the Script

To run the GUI application, execute the Python script directly:

```
python pdf_to_docx_gui.py
```

This will open a window where you can select a PDF file, specify an output file name, and convert the PDF to DOCX.

### Creating a Standalone Executable

To distribute the application as a standalone executable, follow these steps:

1. Install PyInstaller: `pip install pyinstaller`
2. Package the Application: `pyinstaller --onefile --windowed pdf_to_docx_gui.py`
3. Locate the Executable: `dist/pdf_to_docx_gui` and run it



