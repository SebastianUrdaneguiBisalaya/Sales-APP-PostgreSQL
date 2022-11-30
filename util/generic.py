from PIL import ImageTk, Image
from tkinter import filedialog, PhotoImage, Label

def read_image(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

