#!/usr/bin/env python

from setuptools import setup, find_packages

# Function to read the requirements.txt file
def read_requirements():
    with open('requirements.txt') as req_file:
        return req_file.readlines()

setup(
    name='usefulday',
    version='0.2.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'webp_to_jpg=src.image_processing.webp_to_jpg:main',
            'webp_to_png=src.image_processing.webp_to_png:main',
            'jpg_to_png=src.image_processing.jpg_to_png:main',
            'png_to_jpg=src.image_processing.png_to_jpg:main',
            'img_to_pdf=src.image_processing.img_to_pdf:main',
            'heic_to_jpg=src.image_processing.heic_to_jpg:main',
            'reduce_img_size=src.image_processing.reduce_img_size:main',
            'remove_background=src.image_processing.remove_background:main',
            'merge_pdf=src.file_management.merge_pdf:main',
            'doc_to_pdf=src.file_management.doc_to_pdf:main',
            'pdf_to_doc=src.file_management.pdf_to_doc:main',
        ]
    }
)