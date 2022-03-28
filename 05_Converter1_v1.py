""" Converter trial 1, v1
Based on the 02_Converter_GUIv2
Added commands to buttons - at line 50 and 57
Then added functions for each conversion - line 85-97
By Amy Jorgensen
27/03/22
"""

from tkinter import *


class Converter:
    def __init__(self):
        # Formatting variables
        bg_colour = "#f5e7b5"  # beige

        # Converter Frame
        self.converter_frame = Frame(width=100, bg=bg_colour, pady=10)
        self.converter_frame.grid()

        # Temperature converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font="Arial 14 bold", fg="#3b5e3d",
                                        bg=bg_colour, padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push "
                                                  "one of the buttons below",
                                             font="Arial 10 italic", wrap=250,
                                             justify=LEFT, bg=bg_colour,
                                             fg="#3b5e3d", padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold", justify=CENTER)
        self.to_convert_entry.grid(row=2)

        # Conversion button frame (row 3)
        self.converter_btn_frame = Frame(self.converter_frame, bg=bg_colour)
        self.converter_btn_frame.grid(row=3, pady=10)

        # Celsius button (row 0, column 0)
        self.to_c_btn = Button(self.converter_btn_frame,
                               text="To Centigrade", font="Arial 10 bold",
                               command=self.to_c, bg="#49758c", fg="white",
                               padx=10, pady=10,)
        self.to_c_btn.grid(row=0, column=0, padx=10)

        # Fahrenheit button (row 0, column 0)
        self.to_f_btn = Button(self.converter_btn_frame,
                               text="To Fahrenheit", font="Arial 10 bold",
                               command=self.to_f, bg="#ad5771", fg="white",
                               padx=10, pady=10,)
        self.to_f_btn.grid(row=0, column=1, padx=10)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame,
                                     text="Conversion goes here",
                                     font="Arial 12 bold", fg="#3b5e3d",
                                     bg=bg_colour, pady=10, padx=10)
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_btn_frame = Frame(self.converter_frame, bg=bg_colour)
        self.hist_help_btn_frame.grid(row=5, pady=5)

        # history button (row 0, column 0)
        self.calc_hist_btn = Button(self.hist_help_btn_frame,
                                    text="Calculate History",
                                    font="Arial 10 bold", bg="#558757",
                                    fg="white", width=15)
        self.calc_hist_btn.grid(row=0, column=0, padx=5)

        # help button (row 0, column 1)
        self.help_btn = Button(self.hist_help_btn_frame,
                               text="Help", font="Arial 10 bold",
                               bg="#558757", fg="white", width=5)
        self.help_btn.grid(row=0, column=1, padx=5)

    def to_c(self):
        which = 1
        self.change(which)

    def to_f(self):
        which = 2
        self.change(which)

    def change(self, which):
        if which == 1:
            print("Centigrade result")
        else:
            print("Fahrenheit result")


# MAIN ROUTINE
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
