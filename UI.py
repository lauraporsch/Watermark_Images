from tkinter import *
from constants import *
from tkinter import colorchooser
from PIL import ImageGrab
import tkinter.filedialog


class Window(Tk):
    def __init__(self):
        """creates class Window based on super class Tk, creates basic widgets for UI"""
        super().__init__()
        self.title("Watermark Your Images")
        self.config(bg=DARKBLUE)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))
        self.canvas = Canvas(self)
        self.canvas_width = (self.winfo_screenwidth()) / 2
        self.canvas_height = self.winfo_screenheight()
        self.canvas.config(width=self.canvas_width, height=self.canvas_height)
        self.watermark = 0
        self.text = Entry(self, width=20, font=(FONT, 14))
        self.chosen_font = StringVar(self)
        self.current_font = FONT
        self.chosen_size = Scale(self, orient=HORIZONTAL, length=150, from_=1)
        self.current_size = 30
        self.chosen_rotation = Scale(self, orient=HORIZONTAL, length=150, from_=-180, to=180, resolution=5)

    def open_photo(self, img):
        """opens up the selected image on a Canvas on the left side of the screen, calls the unction watermark_ui to
        display the User Interface"""
        self.canvas.grid(column=0, row=0, rowspan=10)
        self.canvas.create_image((self.canvas_width / 2, self.canvas_height / 2), anchor=CENTER, image=img)
        self.canvas.image = img
        self.watermark = self.canvas.create_text((self.canvas_width / 2, self.canvas_height / 2), text="",
                                                 font=(FONT, self.current_size))
        self.watermark_ui()

    def watermark_ui(self):
        """create User Interface for user to choose watermark and configure watermark attributes"""

        description_label = Label(self, text="Watermark your Image", font=(FONT, 40), fg=LIGHTBLUE, bg=DARKBLUE)
        description_label.grid(column=1, row=0, columnspan=2)
        description_label.config(padx=80)

        text_label = Label(self, text="Text:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
        text_label.grid(column=1, row=1)

        self.text.insert(END, string="Text for your watermark.")
        self.text.grid(column=2, row=1)

        show_button = Button(self, text="Show Watermark", highlightthickness=0, height=2, width=20, bg=LIGHTGREEN,
                             fg=DARKBLUE, font=(FONT, 10, "bold"), command=self.show_watermark)
        show_button.grid(column=2, row=2)

        color_label = Label(self, text="Color:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
        color_label.grid(column=1, row=3)
        color = Button(self, text="Choose Color", highlightthickness=0, height=1, width=20, fg=DARKBLUE,
                       font=(FONT, 10, "bold"), command=self.choose_color)
        color.grid(column=2, row=3)

        font_label = Label(self, text="Font:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
        font_label.grid(column=1, row=4)

        self.chosen_font.set("        Choose Font        ")
        font_options = OptionMenu(self, self.chosen_font, *FONTS)
        button_font = Button(text="OK", command=self.change_font)
        font_options.grid(column=2, row=4)
        button_font.place(x=1380, y=365)

        size_label = Label(self, text="Size:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
        size_label.grid(column=1, row=5)

        current_size = Button(text="OK", command=self.change_size)
        self.chosen_size.set(self.current_size)
        self.chosen_size.grid(column=2, row=5)
        current_size.place(x=1380, y=445)

        rotation_label = Label(self, text="Rotation:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
        rotation_label.grid(column=1, row=6)

        rotation_button = Button(text="OK", command=self.change_rotation)
        self.chosen_rotation.grid(column=2, row=6)
        rotation_button.place(x=1380, y=525)

        position_label = Label(self, text="Position:", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
        position_label.grid(column=1, row=7)

        position_canvas = Canvas(self, bg=DARKBLUE, highlightthickness=0)
        position_canvas.grid(column=2, row=7)
        up_button = Button(position_canvas, text=" ⬆ ", command=self.up)
        up_button.config(padx=10, pady=10)
        up_button.grid(column=2, row=0)
        left_button = Button(position_canvas, text="⬅", command=self.left)
        left_button.config(padx=10, pady=10)
        left_button.grid(column=0, row=2)
        center_button = Button(position_canvas, text="○", command=self.center)
        center_button.config(padx=10, pady=10)
        center_button.grid(column=2, row=2)
        right_button = Button(position_canvas, text="➡", command=self.right)
        right_button.config(padx=10, pady=10)
        right_button.grid(column=4, row=2)
        down_button = Button(position_canvas, text=" ⬇ ", command=self.down)
        down_button.config(padx=10, pady=10)
        down_button.grid(column=2, row=4)

        save_button = Button(self, text="SAVE", highlightthickness=0, height=2, width=40, bg=LIGHTGREEN, fg=DARKBLUE,
                             font=(FONT, 10, "bold"), command=self.save_file)
        save_button.grid(column=1, row=8, columnspan=2)

    def show_watermark(self):
        """gets input in Entry field and changes default empty watermark to input"""
        self.canvas.itemconfig(self.watermark, text=self.text.get())

    def choose_color(self):
        """opens color chooser, to choose individual color for watermark"""
        color_code = colorchooser.askcolor(title="Choose color")
        self.canvas.itemconfig(self.watermark, fill=color_code[1])

    def change_font(self):
        """gets the font of choice from drop down menu and changes watermark font to choice"""
        self.current_font = self.chosen_font.get()
        self.canvas.itemconfig(self.watermark, font=(self.current_font, 30))

    def change_size(self):
        """gets current selected size from slider and changes watermark size accordingly"""
        selected_size = self.chosen_size.get()
        self.canvas.itemconfig(self.watermark, font=(self.current_font, selected_size))

    def change_rotation(self):
        """gets current selected rotation from slider and changes watermark rotation accordingly"""
        selected_rotation = self.chosen_rotation.get()
        self.canvas.itemconfig(self.watermark, angle=selected_rotation)

    def up(self):
        """changes anchor of watermark to south, moves position of watermark up"""
        self.canvas.itemconfig(self.watermark, anchor=S)

    def center(self):
        """changes anchor of watermark to center"""
        self.canvas.itemconfig(self.watermark, anchor=CENTER)

    def left(self):
        """changes anchor of watermark to east, moves position of watermark to the left"""
        self.canvas.itemconfig(self.watermark, anchor=E)

    def right(self):
        """changes anchor of watermark to west, moves position of watermark to the right"""
        self.canvas.itemconfig(self.watermark, anchor=W)

    def down(self):
        """changes anchor of watermark to north, moves position of watermark down"""
        self.canvas.itemconfig(self.watermark, anchor=N)

    def save_file(self):
        """creates a screenshot of the canvas including the watermark and saves it under the chosen file path,
        work around as TkInter is limited regarding saving files"""
        left_border = self.winfo_rootx() + self.canvas.winfo_x()
        upper = self.winfo_rooty() + self.canvas.winfo_y()
        right_border = left_border + self.canvas.winfo_width()
        lower = upper + self.canvas.winfo_height()
        files = [('Image Files', '.jpeg .jpg .png')]
        file_path = tkinter.filedialog.asksaveasfile(filetypes=files, defaultextension='.jpeg')
        ImageGrab.grab().crop((left_border, upper, right_border, lower)).save(file_path)
