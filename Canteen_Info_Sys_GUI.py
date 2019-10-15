"""
CX1003 Introduction to Computational Thinking Mini Project
Real-time Canteen Information System
FS1 Bian Hengwei
FS1 Bryan Lim
FS1 Cheng Yu Feng
Functions that represents different pages of the
graphical user interface
Built with Tkinter
"""

from tkinter import *
from Canteen_Info_Sys import *


# initializes data that MUST be initialized in the main() function
def initialize(data):
    data.width, data.height = 600, 400
    data.cover = PhotoImage(file='images/cover.png')


# draws the cover
def cover(root, data):

    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new canvas for the cover page
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(highlightthickness=0)
    canvas.pack()

    # draws a background image
    canvas.create_image(data.width // 2, data.height // 2, image=data.cover)

    # a button that directs to the select store window
    select_stall_button = Button(canvas, text='SELECT STORE',
                                 command=lambda: select_stall(root, data))
    select_stall_button.place(x=data.width // 2, y=data.height * 2 // 3, anchor=CENTER)

    # text
    canvas.create_text(data.width // 2, data.height // 3, text='North Spine Canteen\nInformation System',
                       font='Noteworthy 50 bold italic', fill='white')


# draws a canvas that shows the stalls list
def select_stall(root, data):

    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(highlightthickness=0)
    canvas.pack()

    # draws the background
    canvas.create_image(data.width // 2, data.height // 2, image=data.cover)

    # reads the stalls list
    stalls_list = get_stalls()
    stalls_count = len(stalls_list)

    # builds the buttons
    margin_height = data.height // (stalls_count * 2 + 1)
    button_height = margin_height * 2
    margin_width = 50
    button_width = 225

    # draws and places the buttons
    for stall_name in stalls_list:
        stall_index = stalls_list.index(stall_name)
        if stall_index >= stalls_count // 2:
            x = margin_width * 2 + button_width
            y_index = stall_index - stalls_count // 2
        else:
            x = margin_width
            y_index = stall_index
        y = (y_index + 1) * margin_height + y_index * button_height
        stall = Button(canvas, text=stall_name)
        stall.place(x=x, y=y, width=button_width, height=button_height, anchor=NW)
        stall.config(command=lambda: display_stall(root, data, stall['text']))

    # a back button
    back_button = Button(canvas, text='Back', command=lambda: cover(root, data))
    back_button.place(x=0, y=data.height, anchor=SW)


def display_stall(root, data, stall_name):

    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(highlightthickness=0)
    canvas.pack()

    # draws the background
    canvas.create_image(data.width // 2, data.height // 2, image=data.cover)

    # reads the operating hours and the menu
    stall_info = get_info(stall_name)
    if isinstance(stall_info, str):
        error(root, data, stall_info)
        return

    # displays the stall name and the operating hour
    canvas.create_text(50, 50, text=stall_name, font='40')


# error page
def error(root, data, error_message):

    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new empty canvas with the same width and height
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(highlightthickness=0)
    canvas.pack()

    Button(canvas, text=error_message + '\n\nTernimate', command=root.destroy).place(
        x=data.width // 2, y=data.height //2, anchor=CENTER)


# this is a page template
# copy and paste when creating new pages to save time
def page_template(root, data):

    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(highlightthickness=0)
    canvas.pack()

    # draws the background
    canvas.create_image(data.width // 2, data.height // 2, image=data.cover)

    # a button with common configs edited
    btn = Button(canvas, text='BACK BUTTON', fg='green', bg="#%02x%02x%02x" % (50, 100, 200),
                 font='Times 50 bold italic underline', command=lambda: cover(root, data))
    btn.place(x=data.width // 2, y=data.height // 4, anchor=CENTER)

    # a text label that shows the content entered in the entry
    text_label = Label(canvas, fg='green', font='Georgia 30')
    text_label.place(x=data.width // 2, y=data.height // 2, anchor=CENTER)

    # a string variable that stores the text in entry when enter button is clicked
    entry_input = StringVar(None, 'ENTER SOMETHING!')

    # entry widget
    entry = Entry(canvas, textvariable=entry_input)
    entry.place(x=data.width // 2, y=data.height * 3 // 4, anchor=CENTER, height=20)

    # button that helps display stored information
    btn_enter = Button(canvas, text='ENTER',
                       command=lambda: text_label.config(text='You Entered: ' + entry_input.get(), bg='red'))
    btn_enter.place(x=data.width // 2, y=data.height * 3 // 4 + 20, anchor=CENTER, height=20)

    # returns to the cover
    btn_back = Button(canvas, text='Back', command=lambda: cover(root, data))
    btn_back.place(x=0, y=data.height, anchor=SW)
