#!/usr/bin/env python3

"""


"""

__author__ = 'Rivar Yoder'
__version__ = '1.0'
__date__ = '2025.06.16'
__status__ = 'Development'

from Images import *
import os
from PIL import Image


def main():
    image_list = []
    for filename in os.listdir(Images):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                img = Image.open(os.path.join(Images, filename))
                image_list.append(img)
            except Exception as e:
                print(f"Error loading image {filename}: {e}")



if __name__ == "__main__":
    main()