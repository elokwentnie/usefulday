import sys
import argparse
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS

def extract_img_metadata(input_file: Path) -> None:
    try:
        with Image.open(input_file) as img:
            # Basic image information
            info_dict = {
                "Image Name": input_file.name,
                "Image Size": img.size,
                "Image Height": img.height,
                "Image Width": img.width,
                "Image Format": img.format,
                "Image Mode": img.mode,
                "Is Animated": getattr(img, "is_animated", False),
                "Frames in Image": getattr(img, "n_frames", 1),
            }
            for label, value in info_dict.items():
                print(f"{label:25}: {value}")

            # EXIF data
            exifdata = img.getexif()
            if exifdata:
                print("\nEXIF Data:")
                for tag_id, data in exifdata.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if isinstance(data, bytes):
                        try:
                            data = data.decode()
                        except UnicodeDecodeError:
                            data = data.decode('latin1', 'ignore')
                    print(f"{tag:25}: {data}")
            else:
                print("No EXIF data found.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Image.UnidentifiedImageError:
        print(f"Error: Cannot identify image file '{input_file}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Extract metadata from an image file.")
    parser.add_argument('input_file', type=Path, help='Path to the input image file')
    args = parser.parse_args()

    input_file = args.input_file

    # Validate the input file
    if not input_file.is_file():
        print(f"Error: '{input_file}' does not exist or is not a file.")
        sys.exit(1)

    extract_img_metadata(input_file)

if __name__ == '__main__':
    main()