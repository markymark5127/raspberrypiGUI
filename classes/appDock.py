from Tkinter import *
from app import App
from appIcon import AppIcon

# contains a grid of apps max 8 apps
# pageNum contains this pages number
# mainApps is the main grid of apps in a 2d array comes in to constructor as a 1d array
# dock apps is a 1d array for the dockApps


class AppDock:

    def __init__(self, dock_apps, root):
        self.root = root
        self.dockApps = dock_apps
        for i in range(len(self.dockApps)):
            if len(self.dockApps) > i:
                self.dockApps[i].icon.frame.grid(row=0, column=i, sticky="wens")
                # self.dockApps[i].icon.appIcon.grid(sticky="wens")
            #else:
                #blank = App(AppIcon("blank", "blank", root))
               # blank.icon.root.grid(row=0, column=i, sticky="wens")
                # blank.icon.appIcon.grid(sticky="wens")
