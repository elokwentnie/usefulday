import exif
from PIL import Image
import sys
import argparse
import os

def change_img_metadata(input_file):
    try:    
        img = exif.Image(input_file)
        exifdata = img.get_all()
        
        for tag in exifdata:
            print(f"{tag} : {img.get(tag)}")
            print(img.tag)

        # Save the image with the new EXIF data
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}-changed.jpg"
        # img.save(output_file, exif=img.info.get('exif'))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def is_image(file_path):
    try:
        with Image.open(file_path) as img:
            return True
    except (IOError, Image.UnidentifiedImageError) as e:
        print(f"Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Change metadata from .jpg image")
    parser.add_argument('input_file', metavar='input_file', type=str, default=None, help='Input image (jpg) file path')
    
    args = parser.parse_args()

    if os.path.isfile(args.input_file) and is_image(args.input_file) and (args.input_file.lower().endswith('.jpg') or args.input_file.lower().endswith('.jpeg')):
        change_img_metadata(args.input_file)
    else:
        print(f"Error: {args.input_file} does not exist or the file is not an .jpg image.")
        sys.exit(1)

if __name__ == '__main__':
    main()