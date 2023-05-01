from tkinter import *
import tkinter.filedialog
from tkinter import colorchooser
from PIL import Image, ImageTk, ImageGrab


# ---------------------------- CONSTANTS ------------------------------- #
DARKBLUE = "#0A4D68"
DARKGREEN = "#088395"
LIGHTBLUE = "#05BFDB"
LIGHTGREEN = "#00FFCA"
FONT = "Arial"
FONTS = ["Arial", "Courier", "Georgia", "Impact", "Tahoma", "Verdana"]


# ---------------------------- WELCOME FRAME ------------------------------- #
def welcome():
    """creates Frame with first screen to be seen by user"""
    frame = Frame(window, bg=DARKBLUE)
    welcome_label = Label(frame, text="WELCOME", font=("Georgia", 50, "bold"), fg=LIGHTGREEN, bg=DARKBLUE)
    welcome_label.grid(column=1, row=0)
    welcome_label.config(pady=30, padx=500)

    instruction_label = Label(frame, text="Use this program to watermark any of your images with an individual "
                                          "text", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
    instruction_label.grid(column=1, row=1)
    instruction_label.config(pady=50)

    # Create upload spot for image-file
    upload_label = Label(frame, text="Please upload your image as .jpeg, .jpg or .png file",
                         font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
    upload_label.grid(column=0, row=2, columnspan=2)
    upload_label.config(pady=20)

    upload_button = Button(frame, text="UPLOAD", highlightthickness=0, height=2, width=10,
                           background=LIGHTGREEN, foreground=DARKBLUE, font=(FONT, 10, "bold"), command=upload_file)
    upload_button.grid(column=1, row=3, columnspan=2)
    return frame


# ---------------------------- UPLOAD FILE ------------------------------- #
def upload_file():
    """open up dialog window to choose file from computer and get file path"""
    file_path = tkinter.filedialog.askopenfilename(filetypes=[('Image Files', '.jpeg .jpg .png')])
    img = ImageTk.PhotoImage(Image.open(file_path))
    # clears window
    welcome_frame.destroy()
    # creates canvas that opens up the image on left half of the screen
    canvas_width = (window.winfo_screenwidth())/2
    canvas_height = window.winfo_screenheight()
    canvas = Canvas(window, width=canvas_width, height=canvas_height)
    canvas.grid(column=0, row=0, rowspan=10)
    canvas.create_image((canvas_width/2, canvas_height/2), anchor=CENTER, image=img)
    canvas.image = img
    watermark = canvas.create_text((canvas_width/2, canvas_height/2), text="", font=(FONT, 30))
    watermark_ui(canvas, watermark)


# ---------------------------- CHOOSE COLOR ------------------------------- #
def choose_color(canvas, watermark):
    """opens color chooser, to choose individual color for watermark"""
    color_code = colorchooser.askcolor(title="Choose color")
    canvas.itemconfig(watermark, fill=color_code[1])


# ---------------------------- CHOOSE FONT ------------------------------- #
def get_font(chosen_font):
    """gets the current font of choice from drop down menu"""
    # individual function, so it can be reused in other context
    # (e.g. change size, opacity without loosing current choice)
    selected_font = chosen_font.get()
    return selected_font


def change_font(canvas, watermark, chosen_font):
    """gets the font of choice from drop down menu and changes watermark font to choice"""
    selected_font = get_font(chosen_font)
    canvas.itemconfig(watermark, font=selected_font)


# ---------------------------- CHANGE SIZE ------------------------------- #
def change_size(canvas, watermark, chosen_size, chosen_font):
    """gets current selected size from slider and changes watermark size accordingly"""
    selected_size = chosen_size.get()
    current_font = get_font(chosen_font)
    canvas.itemconfig(watermark, font=(current_font, selected_size))


# ---------------------------- CHANGE ROTATION ------------------------------- #
def change_rotation(canvas, watermark, chosen_rotation):
    """gets current selected rotation from slider and changes watermark rotation accordingly"""
    selected_rotation = chosen_rotation.get()
    canvas.itemconfig(watermark, angle=selected_rotation)


# ---------------------------- CHANGE POSITION ------------------------------- #
def center(canvas, watermark):
    canvas.itemconfig(watermark, anchor=CENTER)


def up(canvas, watermark):
    canvas.itemconfig(watermark, anchor=S)


def left(canvas, watermark):
    canvas.itemconfig(watermark, anchor=E)


def right(canvas, watermark):
    canvas.itemconfig(watermark, anchor=W)


def down(canvas, watermark):
    canvas.itemconfig(watermark, anchor=N)


# ---------------------------- SAVE WATERMARKED IMAGE ------------------------------- #
def save_file(canvas):
    left_border = window.winfo_rootx() + canvas.winfo_x()
    upper = window.winfo_rooty() + canvas.winfo_y()
    right_border = left_border + canvas.winfo_width()
    lower = upper + canvas.winfo_height()
    files = [('Image Files', '.jpeg .jpg .png')]
    file_path = tkinter.filedialog.asksaveasfile(filetypes=files, defaultextension='.jpeg')
    ImageGrab.grab().crop((left_border, upper, right_border, lower)).save(file_path)
    # ImageGrab.grab().crop(left, upper, right, lower).save(file_path)


# ---------------------------- WATERMARK UI ------------------------------- #
def watermark_ui(canvas, watermark):
    """create UI for user to choose watermark and configure watermark attributes"""

    description_label = Label(window, text="Watermark your Image", font=(FONT, 40), fg=LIGHTBLUE, bg=DARKBLUE)
    description_label.grid(column=1, row=0, columnspan=2)
    description_label.config(padx=80)

    # Creating Label and Entry field for choosing text of watermark, show button displays the text on the uploaded image
    text_label = Label(window, text="Text:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
    text_label.grid(column=1, row=1)

    text = Entry(window, width=20, font=(FONT, 14))
    text.insert(END, string="Text for your watermark.")
    text.grid(column=2, row=1)

    show_button = Button(window, text="Show Watermark", highlightthickness=0, height=2, width=20, background=LIGHTGREEN,
                         foreground=DARKBLUE, font=(FONT, 10, "bold"),
                         command=lambda: show_watermark(text, canvas, watermark))
    show_button.grid(column=2, row=2)

    # create Label and button to choose color of watermark, color changes as soon as user chose
    color_label = Label(window, text="Color:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
    color_label.grid(column=1, row=3)
    color = Button(window, text="Choose Color", highlightthickness=0, height=1, width=20, foreground=DARKBLUE,
                   font=(FONT, 10, "bold"), command=lambda: choose_color(canvas, watermark))
    color.grid(column=2, row=3)

    # create label and button to choose font of watermark, drop down menu with a choice of fonts
    font_label = Label(window, text="Font:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
    font_label.grid(column=1, row=4)

    chosen_font = StringVar(window)
    chosen_font.set("        Choose Font        ")
    font_options = OptionMenu(window, chosen_font, *FONTS)
    button_font = Button(text="OK", command=lambda: change_font(canvas, watermark, chosen_font))
    font_options.grid(column=2, row=4)
    button_font.place(x=1380, y=365)

    # create label and slider to choose size of font of watermark
    size_label = Label(window, text="Size:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
    size_label.grid(column=1, row=5)

    chosen_size = Scale(window, orient=HORIZONTAL, length=150, from_=1)
    current_size = Button(text="OK", command=lambda: change_size(canvas, watermark, chosen_size, chosen_font))
    chosen_size.grid(column=2, row=5)
    current_size.place(x=1380, y=445)

    # create label and slider to rotate watermark
    rotation_label = Label(window, text="Rotation:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
    rotation_label.grid(column=1, row=6)

    chosen_rotation = Scale(window, orient=HORIZONTAL, length=150, from_=-180, to=180, resolution=5)
    rotation_button = Button(text="OK", command=lambda: change_rotation(canvas, watermark, chosen_rotation))
    chosen_rotation.grid(column=2, row=6)
    rotation_button.place(x=1380, y=525)

    # create label and buttons to change position of watermark on canvas
    position_label = Label(window, text="Position:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
    position_label.grid(column=1, row=7)
    # add extra Canvas for easier positioning of directional buttons
    position_canvas = Canvas(window, bg=DARKBLUE, highlightthickness=0)
    position_canvas.grid(column=2, row=7)
    up_button = Button(position_canvas, text=" ⬆ ", command=lambda: up(canvas, watermark))
    up_button.config(padx=10, pady=10)
    up_button.grid(column=2, row=0)
    left_button = Button(position_canvas, text="⬅", command=lambda: left(canvas, watermark))
    left_button.config(padx=10, pady=10)
    left_button.grid(column=0, row=2)
    center_button = Button(position_canvas, text="○", command=lambda: center(canvas, watermark))
    center_button.config(padx=10, pady=10)
    center_button.grid(column=2, row=2)
    right_button = Button(position_canvas, text="➡", command=lambda: right(canvas, watermark))
    right_button.config(padx=10, pady=10)
    right_button.grid(column=4, row=2)
    down_button = Button(position_canvas, text=" ⬇ ", command=lambda: down(canvas, watermark))
    down_button.config(padx=10, pady=10)
    down_button.grid(column=2, row=4)

    # create button to save image including the watermark
    save_button = Button(window, text="SAVE", highlightthickness=0, height=2, width=40, background=LIGHTGREEN,
                         foreground=DARKBLUE, font=(FONT, 10, "bold"), command=lambda: save_file(canvas))
    save_button.grid(column=1, row=8, columnspan=2)

    return text


def show_watermark(text, canvas, watermark):
    """gets input in Entry field and changes default empty watermark to input"""
    canvas.itemconfig(watermark, text=text.get())


# ---------------------------- UI SETUP ------------------------------- #
# create screen window with tkinter application
window = Tk()
# window layout
window.title("Watermark Your Images")
window.config(bg=DARKBLUE)
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

# welcome-frame
welcome_frame = welcome()
welcome_frame.pack(fill="both", expand=True)


# keep window open
window.mainloop()
