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
    # Specify the path for the new directory
    source_folder = "./Images"
    destination_folder = "./Renamed_Images"

    # Create the directory
    try:
        shutil.copytree(source_folder, destination_folder)
    except FileExistsError:
        print(f"Directory '{destination_folder}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{destination_folder}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return


def rename_images():
    directory = "./Images"
    current_year = datetime.now().year

    # Iterate over all files in the directory
    for i, filename in enumerate(os.listdir(directory)):
        try:
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                # Create the new file name
                # new_name = ("TESTING" + f"_{i}.png")
                new_name = (str(current_year) + f"_{i}.png")

                # Create the full file path
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_name)

                # Rename the file
                os.rename(old_path, new_path)
            else:
                print("This file is not a .png, .jpg, or .jpeg.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
            print("Images Renamed :)")
        return


def main():
    # copy_folder()
    rename_images()


if __name__ == "__main__":
    main()