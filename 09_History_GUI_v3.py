from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:
    def __init__(self):

        # formatting variables
        background_colour = "light blue"

        # Initialise list to hold calculation history
        # In later versions list will be populated with user calculations
        self.all_calculations = ["0 degrees F is -17.8 degrees C",
                                 "0 degrees C is 32 degrees F",
                                 "40 degrees C is 104 degrees F",
                                 "40 degrees F is 4.4 degrees C",
                                 "12 degrees C is 53.6 degrees F",
                                 "24 degrees C is 75.2 degrees F",
                                 "100 degrees F is 37.8 degrees C"]

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=300,
                                     bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history Button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                  font=("Arial", "14"), padx=10, pady=10,
                                  command=self.history)
        self.history_button.grid(row=1)

    def history(self):
        print("You asked for history")
        get_history = history(self)
        get_history.history_text.configure(text="History text goes here")

class history:
    def __init__(self, partner):
        background = "#f5e7b5"  # beige

        # disable history button
        partner.history_button.config(state=DISABLED)

        # sets up child window (ie. history box)
        self.history_box = Toplevel()

        # if users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history,
                                                           partner))

        # set up GUI frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # set up history heading (row 0)
        self.hist_heading = Label(self.history_frame, text="Calculate History",
                                  font="Arial 18 bold", bg=background)
        self.hist_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent "
                                       "calculations. Please use the export "
                                       "button to create a text file of all "
                                       "your calculations for this session",
                                  font="Arial 10 italic", wrap=250,
                                  justify=LEFT, width=40, bg=background,
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # History output goes here (row 2)


        # Export / Dismiss button frame
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_btn = Button(self.export_dismiss_frame, text="Export",
                                 font="Arial 12 bold")
        self.export_btn.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                 font="Arial 12 bold",
                                 command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
