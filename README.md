# UsefulDay

**UsefulDay** is a versatile command-line utility designed to streamline various image and document processing tasks. With **UsefulDay**, you can easily convert images between formats, manage PDF files, and more, all from the comfort of your command line and what more important **localy** - without sharing your files on any other server.

## Features
* Image Conversion: Convert WebP images to JPG or PNG, and HEIC images to JPG.
* PDF Management: Merge PDFs, convert DOC files to PDFs, and convert PDFs to DOC files.
* Convenient CLI Tools: Utilize easy-to-use command-line tools for efficient processing.

## Installation
To install UsefulDay, follow these steps:

* Clone the Repository
```bash
git clone https://github.com/elokwentnie/usefulday.git
```
* Navigate to the Project Directory
```bash
cd usefulday
```
* Install Dependencies and Package
Ensure you have pip installed. Then, run:
```bash
pip3 install .
```
This command will install UsefulDay and its dependencies as specified in `requirements.txt`.

## Usage
Once installed, **UsefulDay** provides several command-line tools for image and document processing, for example:
* Image Conversion
  * Convert WebP to JPG:
    ```bash
    webp_to_jpg <input_file> <output_file>
    ```
* PDF Management
  * Merge PDFs:
    ```bash
    merge_pdf -f <input_file> <input_file> <input_file> -o <output_file>
    # Example: merge_pdf -f file1.pdf file2.pdf -o merged_output.pdf
    ```

## Additionaly
You can look in `gui` directory to find some of the functionalities ready to create standalone gui application on your Desktop, to say goodbay to Terminal ;) 