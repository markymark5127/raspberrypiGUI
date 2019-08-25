from tkinter import *


class DialpadKeyboard:

    def __init__(self, root):
        self.isCapitals = False
        self.frame = Frame(root, background="white")
        self.frame.pack(fill=X, side=BOTTOM)

        self.button1 = Button(self.frame, width=1, height=1, text="1")
        self.button2 = Button(self.frame, width=1, height=1, text="2")
        self.button3 = Button(self.frame, width=1, height=1, text="3")

        self.button4 = Button(self.frame, width=1, height=1, text="4")
        self.button5 = Button(self.frame, width=1, height=1, text="5")
        self.button6 = Button(self.frame, width=1, height=1, text="6")

        self.button7 = Button(self.frame, width=1, height=1, text="7")
        self.button8 = Button(self.frame, width=1, height=1, text="8")
        self.button9 = Button(self.frame, width=1, height=1, text="9")

        self.returnButton = Button(self.frame, width=1, height=1, text=u"\u23CE")
        self.button0 = Button(self.frame, width=1, height=1, text="0")
        self.deleteButton = Button(self.frame, width=1, height=1, text=u"\u232B")

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)

        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)

        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)

        self.returnButton.grid(row=3, column=0)
        self.button0.grid(row=3, column=1)
        self.deleteButton.grid(row=3, column=2)

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
