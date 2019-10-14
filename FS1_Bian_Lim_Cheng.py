"""
CX1003 Introduction to Computational Thinking Mini Project
Real-time Canteen Information System
FS1 Bian Hengwei
FS1 Bryan Lim
FS1 Cheng Yu Feng
Main file that runs the whole app
"""

from Canteen_Info_Sys_GUI import *


# main func that runs the whole app
def main(width=600, height=400):

    # creates a root obj and its canvas
    root = Tk()
    root.title('North Spine Canteen Information System')
    root.geometry('600x400')
    root.resizable(False, False)

    # draws the cover
    cover(root, width, height)

    # launches the app and block until window is closed
    root.mainloop()


# runs the app
if __name__ == '__main__':
    main()
