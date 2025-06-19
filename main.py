#!/usr/bin/env python3

"""


"""

__author__ = 'Rivar Yoder'
__version__ = '1.0'
__date__ = '2025.06.16'
__status__ = 'Development'


from copy_images import copy_folder
from tkinter import *
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD


def drag_and_drop_interface():
    root = TkinterDnD.Tk()
    root.title("Drag and Drop Image Renamer")
    root.geometry("400x200")

    label = ttk.Label(root, text="Drag and drop a folder containing images here:")
    label.pack(pady=20)

    def drop(event):
        folder_path = event.data
        if folder_path:
            copy_folder(folder_path)
            label.config(text="Images copied and renamed successfully!")

    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', drop)

    root.mainloop()


def main():
    drag_and_drop_interface()


if __name__ == "__main__":
    main()