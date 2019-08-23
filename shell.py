from Tkinter import *
from classes.appPage import AppPage
from classes.keyboard import Keyboard
import time


root = Tk()
root.overrideredirect(True)
# app = FullScreenApp(root)
main = Frame(root, width=385, height=460, background="black")
main.pack_propagate(0)
main.pack()

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
# display.pack(side=TOP, fill=BOTH)
# homePage = AppPage(0, display)
keyboard = Keyboard(main)

root.mainloop()
