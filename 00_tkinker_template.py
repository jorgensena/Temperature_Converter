""" template """
from tkinter import *

class Foo:
    def __init__(self, parent):
        print("I can program :)")


# MAIN ROUTINE
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    smth = Foo(root)
    root.mainloop()
