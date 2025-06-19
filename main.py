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


def user_interface():
    root = Tk()
    root.geometry("400x400")
    root.title("Image Renamer")

    label = Label(root, text="Welcome to Image Renamer!", font=("Arial", 16))
    label.pack(pady=20)

    button = ttk.Button(root, text="Start Renaming Images", command=lambda: [root.destroy(), copy_folder()])
    button.pack(pady=20)

    drag_and_drop_label = Label(root, text="Drag and drop your images into the 'Images' folder.", font=("Arial", 12))
    drag_and_drop_label.pack(pady=10)
    drag_lable

    def on_drag_start(event):
        drag_label.config(bg="yellow")
        event.widget.start_drag()

    # Drag motion event
    def on_drag_motion(event):
        print(f"Dragging: {event.x_root}, {event.y_root}")

    # Drop event
    def on_drop(event):
        drop_label.config(text="Dropped", bg="lightcoral")
        drag_label.config(bg="lightblue")

    root.mainloop()
    copy_folder()


def main():
    user_interface()


if __name__ == "__main__":
    main()