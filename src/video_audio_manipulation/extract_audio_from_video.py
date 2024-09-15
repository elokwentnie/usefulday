import argparse
import os
import cv2
from audio_extract import extract_audio  


def extract_audio_from_video(input_file, format="mp3", output_file=None):
    audio_extensions = ["mp3", "wav", "aac", "ogg", "flac", "m4a",
                        "wma", "alac", "aiff", "opus"]
    try:
        if output_file:
            base, ext = os.path.splitext(output_file)
            if ext.strip('.').lower() not in audio_extensions:
                output_file = f"{output_file}-extracted.{format}"
        else:
            base, _ = os.path.splitext(input_file)
            output_file = f"{base}-extracted.{format}"

        extract_audio(input_path=input_file, output_path=output_file)
        print(f"Audio has been successfully extracted from '{input_file}' and saved as '{output_file}'")
    except Exception as e:
        print(f"Error during audio extraction: {e}")
        exit(1)


def is_video(file_path):
    try:
        video = cv2.VideoCapture(file_path)
        is_opened = video.isOpened()
        video.release()
        return is_opened
    except Exception as e:
        print(f"Error checking if file is a video: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Extract audio from a video file")
    parser.add_argument('input_file', type=str, help='Input video file path')
    parser.add_argument('-o', '--output_file', type=str, default=None, help="Output audio file name")
    parser.add_argument('-f', '--format', type=str, default='mp3',
                        help='Output audio format (mp3, wav, aac, ogg, flac, m4a, wma, alac, aiff, opus)')
    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        print(f"Error: '{args.input_file}' does not exist.")
        exit(1)

    if not is_video(args.input_file):
        print(f"Error: '{args.input_file}' is not a valid video file.")
        exit(1)

    extract_audio_from_video(args.input_file, args.format, args.output_file)


if __name__ == '__main__':
    main()
