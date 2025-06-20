#!/usr/bin/env python3

import os, os.path
import sys
from datetime import datetime
import shutil
from folder_name import global_variable

DESTINATION_FOLDER = global_variable()


def copy_folder():
    """
    current_datetime = datetime.now()
    formatted_timestamp = current_datetime.strftime("%Y-%m-%d_%H%M.%S")
    """
    source_folder = "./Images"
    # destination_folder = ("./RenamedImages_" + formatted_timestamp)

    # Create the directory
    try:
        shutil.copytree(source_folder, DESTINATION_FOLDER)
    except FileExistsError:
        print(f"Directory '{DESTINATION_FOLDER}' already exists.")
        return None
    except PermissionError:
        print(f"Permission denied: Unable to create '{DESTINATION_FOLDER}'.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    else:
        rename_images(DESTINATION_FOLDER)
        return DESTINATION_FOLDER
        # ask_user_file_download(directory_download)


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
                continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
            print("Image", filename, "renamed to", new_name)
    return directory


def file_download():
    # Downloads folder to computer on both mac and windows
    if sys.platform.startswith('darwin'):
        directory_download = os.path.join(os.path.expanduser('~'), 'Downloads', DESTINATION_FOLDER)
    elif sys.platform.startswith('win32'):
        directory_download = os.path.join(os.path.expanduser('~'), 'Downloads', DESTINATION_FOLDER)
    else:
        directory_download = os.path.join(os.getcwd(), DESTINATION_FOLDER)

    if not os.path.exists(directory_download):
        os.makedirs(directory_download)
