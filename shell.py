from tkinter import *
from classes.appPage import AppPage
from classes.englishKeyboard import EnglishKeyboard
from classes.numericKeyboard import NumericKeyboard
from classes.dialpadKeyboard import DialpadKeyboard
from classes.fullScreenApp import FullScreenApp
import time


root = Tk()
# below command stops the window buttons from displaying
root.overrideredirect(True)
# app = FullScreenApp(root)
main = Frame(root, width=320, height=480, background="black")
# main = Frame(root, background="black")
main.pack_propagate(0)
main.pack(fill=None, expand=False)

# status bar
time1 = ''
status = Label(main, fg="white", bg="black")
status.pack(side=TOP)


# make label update for the time in the status bar
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%A, %B %d, %I:%M %p')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        status.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    status.after(200, tick)

# call the function to update status bar
tick()

# commenting out for keyboard
# Display area
# display = Frame(main, background="black")
# display.pack(fill=BOTH, expand=True)
# homePage = AppPage(0, display)
# keyboard = EnglishKeyboard(main)
keyboard = DialpadKeyboard(main)

root.mainloop()
