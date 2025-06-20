#!/usr/bin/env python3

"""


"""

__author__ = 'Rivar Yoder'
__version__ = '1.0'
__date__ = '2025.06.16'
__status__ = 'Development'

import os
import shutil
from datetime import datetime
from copy_images import copy_folder
from copy_images import file_download
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD


def drag_and_drop_interface():
    root = TkinterDnD.Tk()
    root.title("Drag and Drop Image Renamer")
    root.geometry("400x200")

    label = ttk.Label(root, text="Drag and drop a folder containing images here:")
    label.pack(pady=20)


    def drop(event):
        image_extensions = ('.png', '.jpg', '.jpeg')
        images_folder = 'Images'
        try:
            os.makedirs(images_folder, exist_ok=True)
            files = root.tk.splitlist(event.data)
            copied = False
            rename_images_button()
        except Exception as e:
            label.config(text=f"Error creating folder: {e}")
            return
        for file_path in files:
            if os.path.isdir(file_path):
                for entry in os.listdir(file_path):
                    entry_path = os.path.join(file_path, entry)
                    if os.path.isfile(entry_path) and entry_path.lower().endswith(image_extensions):
                        dest = os.path.join(images_folder, os.path.basename(entry_path))
                        shutil.copy2(entry_path, dest)
                        copied = True
            elif os.path.isfile(file_path) and file_path.lower().endswith(image_extensions):
                dest = os.path.join(images_folder, os.path.basename(file_path))
                shutil.copy2(file_path, dest)
                copied = True
        if copied:
            label.config(text="Images copied to 'Images' folder!")
        else:
            label.config(text="No valid images found.")


    def rename_images_button():
        button = ttk.Button(root, text="Rename Images", command=copy_folder)
        button.pack(pady=10)

        current_datetime = datetime.now()
        formatted_timestamp = current_datetime.strftime("%Y-%m-%d_%H%M.%S")
        destination_folder = ("./RenamedImages_" + formatted_timestamp)

        download_button(destination_folder)
        exit_program_button()
        return[]

    def download_button(destination_folder):
        button = ttk.Button(root, text="Download Renamed Images", command=file_download(destination_folder))
        button.pack(pady=10)

    def exit_program_button():
        button = ttk.Button(root, text="Exit", command=root.quit)
        button.pack(pady=10)

    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', drop)

    root.mainloop()


def main():
    drag_and_drop_interface()


if __name__ == "__main__":
    main()