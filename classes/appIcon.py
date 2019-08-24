from tkinter import *
# defines the app icons displayed on the pages
# name should be a string displayed don label under app image
# icon will be the image displayed on the app pages

# this will define the button shown ion the home homeScreen


class AppIcon:
    # constructor
    def __init__(self, name, icon_img, root, color):
        self.name = name
        self.iconImg = icon_img
        self.root = root
        self.color = color
        # self.frame = Frame(self.root, height="50", width="50", border=5, background="green")
        self.frame = Frame(self.root, border=5, background="blue") # self.color"")
        # self.appIcon = Button(self.root, height=50, width=50, text=self.name, bg='white')
        self.appIcon = Button(self.frame, text=self.name, highlightbackground=self.color)
        #self.frame.propagate(0)
        self.appIcon.pack(fill=BOTH, expand=0)
        #self.appIcon.propagate(0)

