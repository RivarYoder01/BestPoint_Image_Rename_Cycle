#!/usr/bin/env python3

"""


"""

__author__ = 'Rivar Yoder'
__version__ = '1.0'
__date__ = '2025.06.16'
__status__ = 'Development'

import os, os.path
from datetime import datetime
import shutil


def copy_folder():
    current_datetime = datetime.now()
    formatted_timestamp = current_datetime.strftime("%Y%m%d_%H%M%S")

    source_folder = "./Images"
    destination_folder = ("./RenamedImages_" + formatted_timestamp)

    # Create the directory
    try:
        shutil.copytree(source_folder, destination_folder)
    except FileExistsError:
        print(f"Directory '{destination_folder}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{destination_folder}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        rename_images(destination_folder)


def rename_images(destination_folder):
    directory = destination_folder
    current_year = datetime.now().year

    # Iterate over all files in the directory
    for i, filename in enumerate(os.listdir(directory)):
        try:
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                # Create the new file name
                new_name = (str(current_year) + f"_{i}.png")

                # Create the full file path
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_name)

                # Rename the file
                os.rename(old_path, new_path)
            else:
                print("This file is not a .png, .jpg, or .jpeg.")
                break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
            print("Image", filename, "renamed to", new_name)

def main():
    copy_folder()

if __name__ == "__main__":
    main()