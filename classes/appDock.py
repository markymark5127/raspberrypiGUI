from tkinter import *
from .app import App
from .appIcon import AppIcon

# contains a grid of apps max 8 apps
# pageNum contains this pages number
# mainApps is the main grid of apps in a 2d array comes in to constructor as a 1d array
# dock apps is a 1d array for the dockApps


class AppDock:

    def __init__(self, dock_apps, root):
        self.root = root
        self.dockApps = dock_apps
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            if len(self.dockApps) > i:

                self.dockApps[i].icon.appIcon.grid(row=0, column=i, sticky="wens")
            else:
                blank = Button(self.root, "", highlightbackground="gray")
                blank.grid(row=0, column=i, sticky="wens")
