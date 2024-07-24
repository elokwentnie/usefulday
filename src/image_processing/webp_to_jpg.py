from PIL import Image
import sys

def webp_to_jpg(input_path, output_path=None):
    if input("Background color: black or white: ").lower() == "white":
        background_color=(255,255,255)
    else:
        background_color=(0,0,0)
    if output_path==None:
        output_path=input_path.split(".")[0] + ".jpg"
    im = Image.open(input_path).convert("RGBA")
    background = Image.new("RGB", im.size, background_color)
    background.paste(im, (0,0), im)

    background.save(output_path, "jpeg"),

def main():
    if len(sys.argv) < 2:
        print("Usage: webp_to_jpg <input_path> [output_path]")
        print(f"Arguments received: {sys.argv}")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    webp_to_jpg(input_path, output_path)

if __name__ == '__main__':
    main()