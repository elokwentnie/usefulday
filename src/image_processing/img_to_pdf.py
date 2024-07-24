from PIL import Image
import img2pdf
import PyPDF2
import sys

def img_to_pdf(input_path, output_path=None):
    if output_path==None:
        output_path=input_path.split(".")[0] + ".pdf"
    with Image.open(input_path) as image:
        pdf = img2pdf.convert(image.filename)
        with open(output_path, "wb") as file:
            file.write(pdf)
            print(f"Converted {input_path} to {output_path}")
    

def main():
    if len(sys.argv) < 2:
        print("Usage: img_to_pdf <input_path> [output_path]")
        print(f"Arguments received: {sys.argv}")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    img_to_pdf(input_path, output_path)

if __name__ == '__main__':
    main()