#!/usr/bin/env python

from setuptools import setup, find_packages

# Function to read the requirements.txt file
def read_requirements():
    with open('requirements.txt') as req_file:
        return req_file.readlines()

setup(
    name='LocalMorph',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'webp_to_jpg=src.image_processing.webp_to_jpg:main',
            'webp_to_png=src.image_processing.webp_to_png:main',
            'jpg_to_png=src.image_processing.jpg_to_png:main',
            'png_to_jpg=src.image_processing.png_to_jpg:main',
            'tiff_to_jpg=src.image_processing.tiff_to_jpg:main',
            'img_to_pdf=src.image_processing.img_to_pdf:main',
            'img_to_greyscale=src.image_processing.img_to_greyscale:main',
            'heic_to_jpg=src.image_processing.heic_to_jpg:main',
            'reduce_img_size=src.image_processing.reduce_img_size:main',
            'remove_background=src.image_processing.remove_background:main',
            'extract_img_metadata=src.image_processing.extract_img_metadata:main',
            'extract_text_from_img=src.image_processing.extract_text_from_img:main',

            'merge_pdf=src.file_management.merge_pdf:main',
            'add_watermark=src.file_management.add_watermark:main',
            'doc_to_pdf=src.file_management.doc_to_pdf:main',
            'pdf_to_doc=src.file_management.pdf_to_doc:main',
            'split_pdf=src.file_management.split_pdf:main',
            'pdf_to_png=src.file_management.pdf_to_png:main',
            'pdf_to_jpg=src.file_management.pdf_to_jpg:main',
            'csv_to_excel=src.file_management.csv_to_excel:main',
            'excel_to_csv=src.file_management.excel_to_csv:main',
            'csv_to_json=src.file_management.csv_to_json:main',
            'json_to_csv=src.file_management.json_to_csv:main',

            'extract_audio_from_video=src.video_audio_manipulation.extract_audio_from_video:main',
        ]
    }
)