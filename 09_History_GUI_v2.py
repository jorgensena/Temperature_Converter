""" Copy of Converter trial 2, v3
By Amy Jorgensen
28/03/22
"""

from tkinter import *
from functools import partial


class Converter:
    def __init__(self):
        # Formatting variables
        bg_colour = "#f5e7b5"  # beige

        # Initialise list to hold calculation history
        # In later versions list will be populated with user calculations
        self.all_calculations = ["0 degrees F is -17.8 degrees C",
                                 "0 degrees C is 32 degrees F",
                                 "40 degrees C is 104 degrees F",
                                 "40 degrees F is 4.4 degrees C",
                                 "12 degrees C is 53.6 degrees F",
                                 "24 degrees C is 75.2 degrees F",
                                 "100 degrees F is 37.8 degrees C"]

        # Converter Frame
        self.converter_frame = Frame(bg=bg_colour, pady=10)
        self.converter_frame.grid()

        # Temperature converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font="Candara 20 bold", fg="#3b5e3d",
                                        bg=bg_colour, padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push "
                                                  "one of the buttons below",
                                             font="Arial 10 italic", wrap=290,
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
                               bg="#49758c", fg="white", padx=10, pady=10,
                               command=lambda: self.temp_convert(-459))
        self.to_c_btn.grid(row=0, column=0, padx=10)

        # Fahrenheit button (row 0, column 0)
        self.to_f_btn = Button(self.converter_btn_frame,
                               text="To Fahrenheit", font="Arial 10 bold",
                               bg="#ad5771", fg="white", padx=10, pady=10,
                               command=lambda: self.temp_convert(-273))
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

    def temp_convert(self, low):
        print(low)

        error = "#ebc091"  # Pale orange bg for when entry box has an error

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        # Check amount is valid
        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check amount is valid and convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = f"{to_convert} degrees C is {fahrenheit} degrees F"

            # Check amount is valid and convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = f"{to_convert} degrees F is {celsius} degrees C"

            else:
                # If input is invalid (e.g. too cold)
                answer = "Too Cold!"
                has_errors = "yes"

            # Display answer
            if has_errors == "no":
                # fg is a purple colour
                self.converted_label.configure(text=answer, fg="#a56bb5")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add answer to list for history
            if answer != "Too Cold":
                self.all_calculations.append(answer)
                print(self.all_calculations)

        except ValueError:
            self.converted_label.configure(text="Enter a number!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)
        return rounded


# MAIN ROUTINE
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    smth = Converter()
    root.mainloop()
