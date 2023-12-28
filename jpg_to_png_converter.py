#!/usr/bin/python3
"""
    JPG to PNG Converter.
    Converts all JPG files in a folder to PNG format and saves them in a new folder.

    Args:
        Images Folder
        Output Folder

    Returns:
        Output folder containing converter image files

    Example Usage:
        python3 jpg_to_png_converter.py

    Code Analysis:
        This script takes 2 arguments (Images folder and Output folder)
        converts all JPG files in the  Image folder to PNG format.
        It creates a new folder named "png_images" if it doesn't already exist.
        It uses the PIL library to open each JPG file, extracts the file name without the extension, 
        and saves the image in PNG format with the same name in the new folder.
        After each conversion, it prints "Done".
"""

import sys
import os
from PIL import Image

folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for file in os.listdir(folder):
    img = Image.open(f'{folder}/{file}')
    clean_name = os.path.splitext(file)

    img.save(f'{new_folder}/{clean_name[0]}.png')

    print(f"{file} Converted Successfully!")
