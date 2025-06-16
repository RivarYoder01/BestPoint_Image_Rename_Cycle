#!/usr/bin/env python3

"""


"""

__author__ = 'Rivar Yoder'
__version__ = '1.0'
__date__ = '2025.06.16'
__status__ = 'Development'

import os


def main():
    img_dir = "BestPoint_Image_Rename_Cycle/Images"

    image_list = []
    for filename in os.listdir(img_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_list.append(os.path.join(img_dir, filename))

    print(image_list)


if __name__ == "__main__":
    main()