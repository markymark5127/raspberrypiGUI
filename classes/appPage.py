from tkinter import *
from .app import App
from .appIcon import AppIcon
from .appDock import AppDock

# contains a grid of apps max 8 apps
# pageNum contains this pages number
# mainApps is the main grid of apps in a 2d array comes in to constructor as a 1d array
# dock apps is a 1d array for the dockApps


class AppPage:

    def __init__(self, page_num, root):
        self.root = root
        self.appFrame = Frame(self.root, background="black")
        self.appFrame.pack(fill=BOTH, expand=1, side=TOP)
        self.dockFrame = Frame(self.root, background="gray")
        self.dockFrame.pack(fill=X, expand=1, side=BOTTOM)

        self.appGrid = Frame(self.appFrame, background="blue")
        self.appGrid.grid_rowconfigure(0, weight=1)
        self.appGrid.grid_columnconfigure(0, weight=1)
        self.dockGrid = Frame(self.root, background="gray")
        self.dockGrid.grid_rowconfigure(0, weight=1)
        self.dockGrid.grid_columnconfigure(0, weight=1)

        self.mainApp = App(AppIcon("main", "main", self.appGrid, "green"))
        self.mainApps = [self.mainApp]
        self.dockApp = App(AppIcon("dock", "dock", self.dockGrid, "gray"))
        self.dockApps = [self.dockApp]
        self.dock = AppDock(self.dockApps, self.dockGrid)
        self.pageNum = page_num

        # fill the main app area with "blank apps" and filled apps
        i = 0
        for r in range(4):
            for c in range(4):
                if len(self.mainApps) > i:
                    self.mainApps[i].icon.frame.grid(row=r, column=c, sticky="wens")
                else:
                    blank = Frame(self.appGrid, border=5, background="white")
                    blank.grid(row=r, column=c, sticky="wens")
                i = i + 1
