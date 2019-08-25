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
        self.appIcon = Button(self.root, text=self.name, height=1, width=1, highlightbackground=self.color)

