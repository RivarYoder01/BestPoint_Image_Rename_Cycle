#!/usr/bin/env python3

"""


"""

__author__ = 'Rivar Yoder'
__version__ = '1.0'
__date__ = '2025.06.16'
__status__ = 'Development'

import os, os.path
from datetime import datetime
# import tkinter as tk
# from tkinter import ttk, filedialog

def rename_images():
    directory = "C:\\Users\\alyss\\PycharmProjects\\BestPoint_Image_Rename_Cycle\\Images"
    current_year = datetime.now().year

    # Iterate over all files in the directory
    for i, filename in enumerate(os.listdir(directory)):
        # Check if the file is an image
        try:
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                # Create the new file name
                new_name = ("AHHHHH" + f"_{i}.png")
                # new_name = (str(current_year) + f"_{i}")

                # Create the full file path
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_name)

                # Rename the file
                os.rename(old_path, new_path)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
            print("Images Renamed :)")


def main():
    rename_images()


if __name__ == "__main__":
    main()