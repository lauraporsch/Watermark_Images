from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk
from welcome import Welcome
from UI import Window


# ---------------------------- UPLOAD FILE ------------------------------- #
def upload_file():
    """open up dialog window to choose file from computer and open file as image in the UI, resize image in case it is
    bigger than the canvas"""
    file_path = tkinter.filedialog.askopenfilename(filetypes=[('Image Files', '.jpeg .jpg .png')])
    original_img = ImageTk.PhotoImage(Image.open(file_path))
    resize_factor = 1
    # if image is smaller than canvas, resize factor stays 1 and image doesn't get altered
    if original_img.width() <= window.canvas_width and original_img.height() <= window.canvas_height:
        pass
    # if image is bigger than canvas resize factor gets changed to percentage of canvas
    else:
        new_width = window.canvas_width / original_img.width()
        new_height = window.canvas_height / original_img.height()
        if new_width < new_height:
            resize_factor *= new_width
        elif new_height < new_width:
            resize_factor *= new_height
    width = int(original_img.width() * resize_factor)
    height = int(original_img.height() * resize_factor)
    img = ImageTk.PhotoImage(Image.open(file_path).resize((width, height)))
    welcome_frame.destroy()
    # create canvas that opens up the image on left half of the screen and the UI on the right side
    window.open_photo(img)


# ---------------------------- UI SETUP ------------------------------- #
window = Window()

# welcome-frame
welcome_frame = Welcome()
welcome_frame.upload_button.config(command=upload_file)

# keep window open
window.mainloop()
