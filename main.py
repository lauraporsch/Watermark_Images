from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk
from welcome import Welcome
from UI import Window


# ---------------------------- UPLOAD FILE ------------------------------- #
def upload_file():
    """open up dialog window to choose file from computer and open file as image in the UI"""
    file_path = tkinter.filedialog.askopenfilename(filetypes=[('Image Files', '.jpeg .jpg .png')])
    img = ImageTk.PhotoImage(Image.open(file_path))
    # clear frame
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
