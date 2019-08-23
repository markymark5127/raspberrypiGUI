from Tkinter import *
from app import App
from appIcon import AppIcon
from appDock import AppDock

# contains a grid of apps max 8 apps
# pageNum contains this pages number
# mainApps is the main grid of apps in a 2d array comes in to constructor as a 1d array
# dock apps is a 1d array for the dockApps


class AppPage:

    def __init__(self, page_num, root):
        self.root = root
        self.appGrid = Frame(self.root, background="black", border=1)
        self.appGrid.pack(fill=BOTH, expand=1, side=TOP)
        self.dockGrid = Frame(self.root, background="gray")
        self.dockGrid.pack(fill=X, expand=1, side=BOTTOM)
        self.mainApp = App(AppIcon("main", "main", self.appGrid, "black"))
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
                    blank = Frame(self.appGrid, height="88", width="96", border=5, background="")
                    blank.grid(row=r, column=c, sticky="wens")
                i = i + 1
