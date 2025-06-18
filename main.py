#!/usr/bin/env python3

"""


"""

__author__ = 'Rivar Yoder'
__version__ = '1.0'
__date__ = '2025.06.16'
__status__ = 'Development'

import os, os.path
import sys
from datetime import datetime
import shutil


def file_download(directory_download):
    print(directory_download)


def ask_user_file_download(directory_download):
    download_newfile = input("Do you want to download your renamed images? (y/n)")
    while download_newfile.isalpha:
        if download_newfile == "y":
            file_download(directory_download)
            sys.exit(0)
        if download_newfile == "n":
            print("Goodbye.")
            sys.exit(0)
        else:
            download_newfile = input("Please input 'y' or 'n'")


def copy_folder():
    current_datetime = datetime.now()
    formatted_timestamp = current_datetime.strftime("%Y-%m-%d_%H%M.%S")

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
        directory_download = rename_images(destination_folder)
        ask_user_file_download(directory_download)


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
    return directory

def main():
    copy_folder()


if __name__ == "__main__":
    main()