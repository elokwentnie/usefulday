from PIL import Image
from PIL.ExifTags import TAGS
import sys
import argparse
import os
from pathlib import Path

def change_img_metadata(input_file):
    try:    
        image = Image.open(input_file).convert("RGB")
        info_dict = {
            "Image Name": Path(input_file).name,
            "Image Size": image.size,
            "Image Height": image.height,
            "Image Width": image.width,
            "Image Format": image.format,
            "Image Mode": image.mode,
            "Image is Animated": getattr(image, "is_animated", False),
            "Frames in Image": getattr(image, "n_frames", 1)
        }
        for label, value in info_dict.items():
            print(f"{label:25}: {value}")
            if input(f"Do you want to update {label}? (y/n): ").lower() == 'y':
                label = input(f"New {label} values: ")

        exifdata = image.getexif()
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")
            if input(f"Do you want to update {tag}? (y/n): ").lower() == 'y':
                label = input(f"New {tag} value: ")
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