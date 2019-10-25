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
from tkinter import Button

from Canteen_Info_Sys import *


# initializes data that MUST be initialized in the main() function
def initialize(data):
    data.cover = PhotoImage(file='images/cover.png')
    data.time = Time()
    data.time.get_current_time()


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

    # shows current time
    canvas.create_text(data.width // 2, data.height // 6, text=data.time.to_string(),
                       font='Times 30 bold')

    # title text
    canvas.create_text(data.width // 4, data.height // 2, text='North Spine\nCanteen\nInformation\nSystem',
                       font='Noteworthy 60 bold italic', fill='white', justify='center')

    # a button that directs to the select store window
    select_stall_button = Button(canvas, text='SELECT\nSTORE', font='Times 30 bold',
                                 command=lambda: select_stall(root, data))
    select_stall_button.place(x=data.width * 3 // 4, y=data.height // 3,
                              width=300, height=100, anchor=CENTER)

    # Change date button
    change_date_button = Button(canvas, text='View Stores By:\n', font='Times 30 bold',
                                command=lambda: change_date(root, data, time_string.get()))
    change_date_button.place(x=data.width * 3 // 4, y=data.height // 2, width=300, height=100, anchor=CENTER)

    # entry widgets that allows time input
    time_string = StringVar(canvas, data.time.to_string()[5:])
    time_entry = Entry(canvas, textvariable=time_string, font='Times 25 bold', justify='center')
    time_entry.place(x=data.width * 3 // 4, y=data.height // 2 + 30, width=300, height=50, anchor=CENTER)

    # exit button
    Button(canvas, text='Exit', font='Times 30 bold',
           command=root.destroy).place(x=data.width * 3 // 4,
                                       y=data.height * 2 // 3, width=300, height=100, anchor=CENTER)


def change_date(root, data, time_string):
    data.time.change_date(time_string)
    select_stall(root, data)


# draws a canvas that shows the stalls list
def select_stall(root, data):
    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(highlightthickness=0)
    canvas.pack()

    # shows current time
    canvas.create_text(data.width // 2, data.height // 6, text=data.time.to_string(),
                       font='Times 30 bold')

    # reads the stalls list
    stalls_list = get_stalls()
    stalls_count = len(stalls_list)

    # builds the buttons
    margin_height = data.height // (stalls_count * 2 + 1)
    button_height = margin_height * 2
    margin_width = data.width // 7
    button_width = margin_width * 2

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
        stall = Button(canvas, text=stall_name, command=lambda name=stall_name: display_stall(root, data, name))
        stall.place(x=x, y=y, width=button_width, height=button_height, anchor=NW)

    # a back button
    back_button = Button(canvas, text='Back', command=lambda: cover(root, data))
    back_button.place(x=0, y=data.height, anchor=SW)


# error page
def error(root, data, error_message):
    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new empty canvas with the same width and height
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(highlightthickness=0)
    canvas.pack()

    Button(canvas, text=error_message + '\n\nTerminate', command=root.destroy).place(
        x=data.width // 2, y=data.height // 2, anchor=CENTER)

    canvas.create_text(data.width // 2, data.height // 4, text=error_message, font='Times 40')

    Button(canvas, text='Terminate', font='Times 40', command=root.destroy).place(
        x=data.width // 2, y=data.height // 2, anchor=CENTER)

    Button(canvas, text='Restart', font='Times 40', command=lambda: cover(root, data)).place(
        x=data.width // 2, y=data.height * 3 // 4, anchor=CENTER)


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

    # stall name
    canvas.create_text(data.width // 2, 50, text=stall_name, font=('Arial', 40))

    # create the buttons for menu, queue time, operating hours (three functions are under tis one)
    menu_btn = Button(root, text='Menu', width=12, height=2, command=lambda: menu(root))
    menu_btn.place(x=30, y=100, anchor=NW)

    queue_btn = Button(root, text='Queue time', width=12, height=2, command=lambda: queue_time(root))
    queue_btn.place(x=30, y=150, anchor=NW)

    operating_btn = Button(root, text='Operating hours', width=12, height=2, command=lambda: operating_hours(root))
    operating_btn.place(x=30, y=200, anchor=NW)

    # return to select store
    back_button = Button(canvas, text='Back', command=lambda: select_stall(root, data))
    back_button.place(x=0, y=data.height, anchor=SW)


def menu(root):
    # cover two canvas on the page
    canvas_m1 = Canvas(root, bg='skyblue1', width=200, height=250)
    canvas_m1.place(x=150, y=100, anchor=NW)

    canvas_m2 = Canvas(root, bg='skyblue1', width=200, height=250)
    canvas_m2.place(x=350, y=100, anchor=NW)

    # read menu.txt and display menu
    menu_content = Label(root, text='closed', font=('Arial,20'))
    menu_content.place(x=450, y=200, anchor=CENTER)


def queue_time(root):
    # function for showing queue time
    def show_queue_time():
        # get the value from the entry below
        var = queue_enter.get()

        # calculate the queue time(should be changed for each stall)
        var_int = int(var)
        var_int = var_int // 2
        var_str = str(var_int)

        # create a label to show the queuing time message
        show_var = 'Estimated queuing time is: ' + var_str + ' minutes'
        queue_result = Label(root, bg='skyblue1', text=show_var, width=30, height=3, font=('Arial', 20))
        queue_result.place(x=350, y=290, anchor=CENTER)

    # canvas for queue time
    canvas_q = Canvas(root, bg='skyblue1', width=400, height=250)
    canvas_q.place(x=150, y=100, anchor=NW)

    # entering message
    queue_text = Label(root, bg='skyblue1', text="Please enter the number of pax queuing", font=('Arial', 20))
    queue_text.place(x=350, y=160, anchor=CENTER)

    # the entry for the number of queuing people
    queue_enter = Entry(root)
    queue_enter.place(x=310, y=225, anchor=CENTER)

    # a button for calculate the time
    calculate_btn = Button(root, text='Calculate', width=7, height=2, command=show_queue_time)
    calculate_btn.place(x=450, y=225, anchor=CENTER)


def operating_hours(root):
    # two canvas for operating hours
    canvas_op1 = Canvas(root, bg='skyblue1', width=200, height=250)
    canvas_op1.place(x=150, y=100, anchor=NW)

    canvas_op2 = Canvas(root, bg='skyblue1', width=200, height=250)
    canvas_op2.place(x=350, y=100, anchor=NW)

    # label for open or close (do we need this????????????)
    oph = Label(root, text='Wednesday: 10am~10pm', font='Arial,20')
    oph.place(x=250, y=200, anchor=CENTER)
