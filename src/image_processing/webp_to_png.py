from PIL import Image
import sys

def webp_to_png(input_path, output_path=None):
    if output_path==None:
        output_path=input_path.split(".")[0] + ".png"
    im = Image.open(input_path).convert("RGBA")
    im.save(output_path, "png")

def main():
    if len(sys.argv) < 2:
        print("Usage: webp_to_png <input_path> [output_path]")
        print(f"Arguments received: {sys.argv}")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    webp_to_png(input_path, output_path)

if __name__ == '__main__':
    main()