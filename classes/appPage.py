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
        self.appFrame = Frame(self.root, background="green")
        self.appFrame.pack(fill=BOTH, expand=1, side=TOP)
        # self.dockFrame = Frame(self.root, background="gray")
        # self.dockFrame.pack(fill=X, expand=1, side=BOTTOM)

        self.appGrid = Frame(self.appFrame, border=5, background="black")
        self.appGrid.pack(fill=BOTH, expand=1)

        self.dockGrid = Frame(self.appFrame, border=5, background="gray")
        self.dockGrid.pack(fill=X, side=BOTTOM, expand=0)
        # self.dockGrid.grid_rowconfigure(0, weight=1)

        self.mainApp1 = App(AppIcon("main", "main1", self.appGrid, "black"))
        # self.mainApp2 = App(AppIcon("main", "main2", self.appGrid, "black"))
        # self.mainApp3 = App(AppIcon("main", "main3", self.appGrid, "black"))
        # self.mainApp4 = App(AppIcon("main", "main4", self.appGrid, "black"))
        # self.mainApp5 = App(AppIcon("main", "main5", self.appGrid, "black"))
        self.mainApps = [self.mainApp1]
        # , self.mainApp2, self.mainApp3, self.mainApp4, self.mainApp5]
        self.dockApp = App(AppIcon("dock", "dock", self.dockGrid, "gray"))
        self.dockApps = [self.dockApp]
        self.dock = AppDock(self.dockApps, self.dockGrid)
        self.pageNum = page_num

        # fill the main app area with "blank apps" and filled apps
        i = 0
        for r in range(4):
            self.appGrid.grid_rowconfigure(r, weight=1)
            self.appGrid.grid_columnconfigure(r, weight=1)
            for c in range(4):
                if len(self.mainApps) > i:
                    self.mainApps[i].icon.appIcon.grid(row=r, column=c, sticky="wens")
                else:
                    blank = Button(self.appGrid, text="", bg="black", highlightbackground="black")
                    blank.grid(row=r, column=c, sticky="wens")
                i = i + 1
