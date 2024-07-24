from setuptools import setup, find_packages

# Function to read the requirements.txt file
def read_requirements():
    with open('requirements.txt') as req_file:
        return req_file.readlines()

setup(
    name='usefulday',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'webp_to_jpg=src.image_processing.webp_to_jpg:main',
            'webp_to_png=src.image_processing.webp_to_png:main',
            'img_to_pdf=src.image_processing.img_to_pdf:main',
        ]
    }
)