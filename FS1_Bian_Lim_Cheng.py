from tkinter import *


# draws the cover
def cover(root):

    # clears the root
    for frame in root.winfo_children():
        frame.destroy()

    # creates a new frame
    frame = Frame(root)
    frame.place(width=600, height=400)

    # draws a background
    background = PhotoImage(file='images/background.png')
    background_label = Label(frame, image=background)
    background_label.image = background
    background_label.place(x=0, y=0)

    # a text label
    title = Label(frame, text='NAME NEEDED!')
    title.place(x=300, y=200)

    # a button that directs to the select store window
    select_store_button = Button(frame, text='SELECT STORE',
                                 command=lambda: select_store(frame, root))
    select_store_button.place(x=200, y=300)


# draws a frame that shows the stalls list
def select_store(prev_frame, root):

    # clears the root
    for frame in root.winfo_children():
        frame.destroy()

    # creates a new frame
    frame = Frame(root)
    frame.place(width=600, height=400)

    # test buttons
    btn = Button(frame, text='Back', command=lambda: cover(root))
    btn.place(x=300, y=200, width=50, height=30)
    btn2 = Button(frame, text='Destroy', command=lambda: root.destroy())
    btn2.place(x=200, y=300)


# main func that runs the whole app
def main():
    # creates a root obj and its frame
    root = Tk()
    root.title('WHO CAN COME UP WITH AN INTERESTING NAME!!!!!')
    root.geometry('600x400')
    root.resizable(False, False)

    # draws the cover
    cover(root)

    # launches the app and block until window is closed
    root.mainloop()


# runs the app
if __name__ == '__main__':
    main()
