from tkinter import *


# draws the cover
def cover(frame):
    frame.place(relheight=600, relwidth=400)
    background = PhotoImage(file='images/background.png')


# main func that runs the whole app
def main():
    # creates a root obj and its frame
    root = Tk()
    root.geometry('600x400')
    root.resizable(True, True)
    frame = Frame(root)

    # draws the cover
    cover(frame)

    # launch the app and block until window is closed
    root.mainloop()


if __name__ == '__main__':
    main()
