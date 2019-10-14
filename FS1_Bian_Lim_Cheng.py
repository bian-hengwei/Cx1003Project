from tkinter import *


# draws the cover
def cover(root, width, height):
    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new canvas for the cover page
    canvas = Canvas(root)
    canvas.place(width=width, height=height)

    # draws a background image
    background = PhotoImage(file='images/cover.png')
    background_label = Label(canvas, image=background)
    background_label.image = background
    background_label.place(x=width // 2, y=height // 2, anchor=CENTER)

    # a text label
    title = Label(canvas, text='North Spine Canteen Information System')
    title.place(x=width // 2, y=height // 3, anchor=CENTER)

    # a button that directs to the select store window
    select_store_button = Button(canvas, text='SELECT STORE',
                                 command=lambda: select_store(root, width, height))
    select_store_button.place(x=width // 2, y=height * 2 // 3, anchor=CENTER)


# draws a canvas that shows the stalls list
def select_store(root, width, height):
    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new canvas
    canvas = Canvas(root)
    canvas.place(width=width, height=height)

    # test buttons
    btn = Button(canvas, text='Back', command=lambda: cover(root, width, height))
    btn.place(x=width // 2, y=height // 4, anchor=CENTER)
    btn2 = Button(canvas, text='Destroy', command=lambda: root.destroy())
    btn2.place(x=width // 2, y=height // 2, anchor=CENTER)
    btn3 = Button(canvas, text='Template', command=lambda: page_template(root, width, height))
    btn3.place(x=width // 2, y=height * 3 // 4, anchor=CENTER)


# this is a page template
# copy and paste when creating new pages to save time
def page_template(root, width, height):

    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new empty canvas with the same width and height
    canvas = Canvas(root)
    canvas.place(width=width, height=height)

    # draws the background
    background = PhotoImage(file='images/cover.png')
    background_label = Label(canvas, image=background)
    background_label.image = background
    background_label.place(x=width // 2, y=height // 2, anchor=CENTER)

    # a button with common configs edited
    btn = Button(canvas, text='BACK BUTTON', fg='green', bg="#%02x%02x%02x" % (50, 100, 200),
                 font='Times 50 bold italic underline', command=lambda: cover(root, width, height))
    btn.place(x=width // 2, y=height // 4, anchor=CENTER)

    # a text label that shows the content entered in the entry
    text_label = Label(canvas, fg='green', font='Georgia 30')
    text_label.place(x=width // 2, y=height // 2, anchor=CENTER)

    # a string variable that stores the text in entry when enter button is clicked
    entry_input = StringVar(None, 'ENTER SOMETHING!')

    # entry widget
    entry = Entry(canvas, textvariable=entry_input)
    entry.place(x=width // 2, y=height * 3 // 4, anchor=CENTER, height=20)

    # button that helps display stored information
    btn_enter = Button(canvas, text='ENTER',
                       command=lambda: text_label.config(text='You Entered: ' + entry_input.get(), bg='red'))
    btn_enter.place(x=width // 2, y=height * 3 // 4 + 20, anchor=CENTER, height=20)

    # returns to the cover
    btn_back = Button(canvas, text='Back', command=lambda: cover(root, width, height))
    btn_back.place(x=0, y=height, anchor=SW)


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
