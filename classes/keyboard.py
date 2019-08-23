from Tkinter import *


class Keyboard:

    q = 'q'
    w = 'w'
    e = 'e'
    r = 'r'
    t = 't'
    y = 'y'
    u = 'u'
    i = 'i'
    o = 'o'
    p = 'p'
    a = 'a'
    s = 's'
    d = 'd'
    f = 'f'
    g = 'g'
    h = 'h'
    j = 'j'
    k = 'k'
    l = 'l'
    z = 'z'
    x = 'x'
    c = 'c'
    v = 'v'
    b = 'b'
    n = 'n'
    m = 'm'

    def __init__(self, root):
        self.isCapitals = False
        self.frame = Frame(root, background="white", height=224)
        self.frame.pack(side=BOTTOM, fill=X)

        self.firstRow = Frame(self.frame)
        self.firstRow.pack(side=TOP)
        self.secondRow = Frame(self.frame)
        self.secondRow.pack(side=TOP)
        self.thirdRow = Frame(self.frame)
        self.thirdRow.pack(side=TOP)
        self.fourthRow = Frame(self.frame)
        self.fourthRow.pack(side=BOTTOM)

        self.qButton = Button(self.firstRow, text=self.q, highlightbackground="white")
        self.wButton = Button(self.firstRow, text=self.w, highlightbackground="white")
        self.eButton = Button(self.firstRow, text=self.e, highlightbackground="white")
        self.rButton = Button(self.firstRow, text=self.r, highlightbackground="white")
        self.tButton = Button(self.firstRow, text=self.t, highlightbackground="white")
        self.yButton = Button(self.firstRow, text=self.y, highlightbackground="white")
        self.uButton = Button(self.firstRow, text=self.u, highlightbackground="white")
        self.iButton = Button(self.firstRow, text=self.i, highlightbackground="white")
        self.oButton = Button(self.firstRow, text=self.o, highlightbackground="white")
        self.pButton = Button(self.firstRow, text=self.p, highlightbackground="white")
        self.deleteButton = Button(self.firstRow, text=u"\u232B", highlightbackground="white")

        self.tabButton = Button(self.secondRow, text="tab", highlightbackground="white")
        self.aButton = Button(self.secondRow, text=self.a, highlightbackground="white")
        self.sButton = Button(self.secondRow, text=self.s, highlightbackground="white")
        self.dButton = Button(self.secondRow, text=self.d, highlightbackground="white")
        self.fButton = Button(self.secondRow, text=self.f, highlightbackground="white")
        self.gButton = Button(self.secondRow, text=self.g, highlightbackground="white")
        self.hButton = Button(self.secondRow, text=self.h, highlightbackground="white")
        self.jButton = Button(self.secondRow, text=self.j, highlightbackground="white")
        self.kButton = Button(self.secondRow, text=self.k, highlightbackground="white")
        self.lButton = Button(self.secondRow, text=self.l, highlightbackground="white")
        self.returnButton = Button(self.secondRow, text=u"\u23CE", highlightbackground="white")

        self.shiftButton = Button(self.thirdRow, text=u"\u21E7", highlightbackground="white", command=self.swapCase)
        self.zButton = Button(self.thirdRow, text=self.z, highlightbackground="white")
        self.xButton = Button(self.thirdRow, text=self.x, highlightbackground="white")
        self.cButton = Button(self.thirdRow, text=self.c, highlightbackground="white")
        self.vButton = Button(self.thirdRow, text=self.v, highlightbackground="white")
        self.bButton = Button(self.thirdRow, text=self.b, highlightbackground="white")
        self.nButton = Button(self.thirdRow, text=self.n, highlightbackground="white")
        self.mButton = Button(self.thirdRow, text=self.m, highlightbackground="white")
        self.commaButton = Button(self.thirdRow, text=",", highlightbackground="white")
        self.periodButton = Button(self.thirdRow, text=".", highlightbackground="white")
        self.questionButton = Button(self.thirdRow, text="?", highlightbackground="white")

        self.numButton = Button(self.fourthRow, text="123", highlightbackground="white")
        self.spaceBar = Button(self.fourthRow, text="                                         ", highlightbackground="white")
        self.keyboardButton = Button(self.fourthRow, text=u"\u2328", highlightbackground="white")

        self.qButton.grid(row=0, column=0)
        self.wButton.grid(row=0, column=1)
        self.eButton.grid(row=0, column=2)
        self.rButton.grid(row=0, column=3)
        self.tButton.grid(row=0, column=4)
        self.yButton.grid(row=0, column=5)
        self.uButton.grid(row=0, column=6)
        self.iButton.grid(row=0, column=7)
        self.oButton.grid(row=0, column=8)
        self.pButton.grid(row=0, column=9)
        self.deleteButton.grid(row=0, column=10)

        self.tabButton.grid(row=0, column=0)
        self.aButton.grid(row=0, column=1)
        self.sButton.grid(row=0, column=2)
        self.dButton.grid(row=0, column=3)
        self.fButton.grid(row=0, column=4)
        self.gButton.grid(row=0, column=5)
        self.hButton.grid(row=0, column=6)
        self.jButton.grid(row=0, column=7)
        self.kButton.grid(row=0, column=8)
        self.lButton.grid(row=0, column=9)
        self.returnButton.grid(row=0, column=10)

        self.shiftButton.grid(row=0, column=0)
        self.zButton.grid(row=0, column=1)
        self.xButton.grid(row=0, column=2)
        self.cButton.grid(row=0, column=3)
        self.vButton.grid(row=0, column=4)
        self.bButton.grid(row=0, column=5)
        self.nButton.grid(row=0, column=6)
        self.mButton.grid(row=0, column=7)
        self.commaButton.grid(row=0, column=8)
        self.periodButton.grid(row=0, column=9)
        self.questionButton.grid(row=0, column=10)

        self.numButton.grid(row=0, column=0)
        self.spaceBar.grid(row=0, column=1)
        self.keyboardButton.grid(row=0, column=2)

    def capitalize(self):
        self.q = 'Q'
        self.w = 'W'
        self.e = 'E'
        self.r = 'R'
        self.t = 'T'
        self.y = 'Y'
        self.u = 'U'
        self.i = 'I'
        self.o = 'O'
        self.p = 'P'
        self.a = 'A'
        self.s = 'S'
        self.d = 'D'
        self.f = 'F'
        self.g = 'G'
        self.h = 'H'
        self.j = 'J'
        self.k = 'K'
        self.l = 'L'
        self.z = 'Z'
        self.x = 'X'
        self.c = 'C'
        self.v = 'V'
        self.b = 'B'
        self.n = 'N'
        self.m = 'M'

    def lowercase(self):
        self.q = 'q'
        self.w = 'w'
        self.e = 'e'
        self.r = 'r'
        self.t = 't'
        self.y = 'y'
        self.u = 'u'
        self.i = 'i'
        self.o = 'o'
        self.p = 'p'
        self.a = 'a'
        self.s = 's'
        self.d = 'd'
        self.f = 'f'
        self.g = 'g'
        self.h = 'h'
        self.j = 'j'
        self.k = 'k'
        self.l = 'l'
        self.z = 'z'
        self.x = 'x'
        self.c = 'c'
        self.v = 'v'
        self.b = 'b'
        self.n = 'n'
        self.m = 'm'

    def swapCase(self):

        if self.isCapitals:
            self.lowercase()
            self.shiftButton.configure(text=u"\u21E7", highlightbackground="white")
            self.isCapitals = False
        else:
            self.capitalize()
            self.shiftButton.configure(text=u"\u2B06", highlightbackground="gray")
            self.isCapitals = True

        self.qButton.configure(text=self.q)
        self.wButton.configure(text=self.w)
        self.eButton.configure(text=self.e)
        self.rButton.configure(text=self.r)
        self.tButton.configure(text=self.t)
        self.yButton.configure(text=self.y)
        self.uButton.configure(text=self.u)
        self.iButton.configure(text=self.i)
        self.oButton.configure(text=self.o)
        self.pButton.configure(text=self.p)
        self.aButton.configure(text=self.a)
        self.sButton.configure(text=self.s)
        self.dButton.configure(text=self.d)
        self.fButton.configure(text=self.f)
        self.gButton.configure(text=self.g)
        self.hButton.configure(text=self.h)
        self.jButton.configure(text=self.j)
        self.kButton.configure(text=self.k)
        self.lButton.configure(text=self.l)
        self.zButton.configure(text=self.z)
        self.xButton.configure(text=self.x)
        self.cButton.configure(text=self.c)
        self.vButton.configure(text=self.v)
        self.bButton.configure(text=self.b)
        self.nButton.configure(text=self.n)
        self.mButton.configure(text=self.m)
