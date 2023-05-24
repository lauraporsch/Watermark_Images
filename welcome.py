from tkinter import *
from constants import *


class Welcome(Frame):
    def __init__(self):
        """creates class Welcome, based on super class Frame, first screen to be seen by user"""
        super().__init__()
        self.config(bg=DARKBLUE)
        self.pack(fill="both", expand=True)
        self.welcome_label = Label(self, text="WELCOME", font=("Georgia", 50, "bold"), fg=LIGHTGREEN, bg=DARKBLUE)
        self.welcome_label.grid(column=1, row=0)
        self.welcome_label.config(pady=30, padx=500)

        self.instruction_label = Label(self, text="Use this program to watermark any of your images with an individual "
                                                  "text", font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
        self.instruction_label.grid(column=1, row=1)
        self.instruction_label.config(pady=50)

        # Create upload spot for image-file
        self.upload_label = Label(self, text="Please upload your image as .jpeg, .jpg or .png file",
                                  font=(FONT, 20), fg=LIGHTBLUE, bg=DARKBLUE)
        self.upload_label.grid(column=0, row=2, columnspan=2)
        self.upload_label.config(pady=20)

        self.upload_button = Button(self, text="UPLOAD", highlightthickness=0, height=2, width=10, bg=LIGHTGREEN,
                                    fg=DARKBLUE, font=(FONT, 10, "bold"))
        self.upload_button.grid(column=1, row=3, columnspan=2)
