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
    canvas.create_text(data.width // 2, data.height * 9 // 10, text=data.time.to_string(),
                       font='Times 25 bold', fill='white')

    # title text
    canvas.create_text(data.width // 4, data.height // 2 - 20, text='North Spine\nCanteen\nInformation\nSystem',
                       font='Noteworthy 60 bold italic', fill='white', justify='center')

    # a button that directs to the select store window
    select_stall_button = Button(canvas, text='SELECT\nSTORE', font='Times 30 bold',
                                 command=lambda: change_date(root, data, data.time.get_current_time().to_string()[5:]))
    select_stall_button.place(x=data.width * 3 // 4, y=data.height // 3 - 20,
                              width=300, height=120, anchor=CENTER)

    # exit button
    Button(canvas, text='Exit', font='Times 30 bold',
           command=root.destroy).place(x=data.width * 3 // 4,
                                       y=data.height * 2 // 3 - 20, width=300, height=120, anchor=CENTER)

    # a constant for drop-down list
    c = 55

    # date drop-down list
    date = ['01', '02', '03', '04', '05', '06', '07', '08', '09'] + [x for x in range(10, 32)]

    variable1 = StringVar(root)
    variable1.set(data.time.get_current_time().to_string()[5:7])  # default value

    d = OptionMenu(root, variable1, *date)
    d.place(x=605, y=data.height // 2 - 7, width=c, anchor=SW)

    # month drop-down list
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    variable = StringVar(root)
    variable.set(data.time.get_current_time().to_string()[8:11])  # default value

    m = OptionMenu(root, variable, *month)
    m.place(x=605 + c, y=data.height // 2 - 7, width=c, anchor=SW)

    # year drop-down list
    year = [x for x in range(2019, 2030)]

    variable2 = StringVar(root)
    variable2.set(data.time.get_current_time().to_string()[12:16])  # default value

    y = OptionMenu(root, variable2, *year)
    y.place(x=605 + 2 * c, y=data.height // 2 - 7, width=c + 15, anchor=SW)

    # hour drop-down list
    hour = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'] + [x for x in range(10, 24)]

    variable3 = StringVar(root)
    variable3.set(data.time.get_current_time().to_string()[18:20])  # default value

    h = OptionMenu(root, variable3, *hour)
    h.place(x=605 + 3 * c + 15, y=data.height // 2 - 7, width=c, anchor=SW)

    # minute drop-down list
    minute = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'] + [x for x in range(10, 60)]

    variable4 = StringVar(root)
    variable4.set(data.time.get_current_time().to_string()[21:23])  # default value

    mi = OptionMenu(root, variable4, *minute)
    mi.place(x=605 + 4 * c + 15, y=data.height // 2 - 7, width=c, anchor=SW)

    # get all the above drop-down list value
    def get_var():
        d_str = variable1.get()
        m_str = variable.get()
        y_str = variable2.get()
        h_str = variable3.get()
        mi_str = variable4.get()
        time_str = str(d_str) + " " + m_str + " " + str(y_str) + ", " + str(h_str) + ":" + str(mi_str)
        change_date(root, data, time_str)

    # Change date button
    change_date_button = Button(canvas, font='Times 30 bold', text="VIEW STORE BY:\n\nEnter",
                                command=get_var)
    change_date_button.place(x=data.width * 3 // 4, y=data.height // 2 - 20, width=300, height=120, anchor=CENTER)


# changes the time object
# allows user to set time
def change_date(root, data, time_str):
    try:
        data.time.change_date(time_str)
        select_stall(root, data)

    # handle date out of month error
    except ValueError:
        # create a pop up window for error message
        window = Tk()
        window.title('ERROR')
        window.geometry('300x70')
        err = Label(window, text='Date is out of range for month.\nPlease try again!')
        err.pack()

        # close error window button
        errbtn = Button(window, text='Close', font='12', command=window.destroy)
        errbtn.pack()


# draws a canvas that shows the stalls list
def select_stall(root, data):
    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(highlightthickness=0)
    canvas.pack()

    # draws a background image
    canvas.create_image(data.width // 2, data.height // 2, image=data.cover)

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
        stall = Button(canvas, text=stall_name, font='Times 25 bold',
                       command=lambda name=stall_name: menu(root, data, name))
        stall.place(x=x, y=y + 40, width=button_width, height=button_height, anchor=NW)

    # a back button
    back_button = Button(canvas, text='BACK', font='Times 30 bold', command=lambda: cover(root, data))
    back_button.place(x=0, y=data.height, width=100, height=80, anchor=SW)

    # shows current time
    canvas.create_text(data.width // 2, data.height * 9 // 10, text=data.time.to_string(),
                       font='Times 25 bold', fill='white')


# error page
def error(root, data, error_message='ERROR'):
    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new empty canvas with the same width and height
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(highlightthickness=0)
    canvas.pack()

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

    # menu button
    menu_button = Button(canvas, text='Menu', font='Times 20', command=lambda: menu(root, data, stall_name))
    menu_button.place(x=data.width // 3, y=data.height // 15, width=data.width // 10,
                      height=data.height // 15, anchor=CENTER)
    # queue time button
    queue_time_button = Button(canvas, text='Queue\nTime', font='Times 20',
                               command=lambda: queue_time(root, data, stall_name))
    queue_time_button.place(x=data.width // 2, y=data.height // 15, width=data.width // 10,
                            height=data.height // 15, anchor=CENTER)
    # operating hours button
    operating_hours_button = Button(canvas, text='Operating\nHours',
                                    font='Times 20', command=lambda: operating_hours(root, data, stall_name))
    operating_hours_button.place(x=data.width * 2 // 3, y=data.height // 15, width=data.width // 10,
                                 height=data.height // 15, anchor=CENTER)

    # stall name
    canvas.create_text(data.width // 2, data.height // 7 + 15, text=stall_name, font='Chalkduster 60', fill='white')

    # a back button
    back_button = Button(canvas, text='BACK', font='Times 30 bold', command=lambda: select_stall(root, data))
    back_button.place(x=0, y=data.height, width=100, height=80, anchor=SW)

    return canvas


def menu(root, data, stall_name):
    canvas = display_stall(root, data, stall_name)

    # reads the stalls info (bryan)
    info_list = get_info(stall_name)[1]

    XBASE, YBASE, DISTANCE = 150, 20, 50
    for i, word in enumerate(info_list):
        canvas.create_text((XBASE, 300 + YBASE + i * DISTANCE), text=word, anchor=W, font='Arial 30')


def queue_time(root, data, stall_name):
    canvas = display_stall(root, data, stall_name)

    # function for showing queue time
    def show_queue_time():
        # get the value from the entry below
        ppl = queue_enter.get()
        queue = {"McDonald's": 0.4, "The Sandwich Guys": 1.5, "Japanese Korean Delight": 1.1, "Vietnamese Cuisine": 1.4,
                 "Malay BBQ": 1.25, "Cantonese Roast Duck": 0.8}

        # calculate the queue time
        ppl_int = int(ppl)
        minute = int(ppl_int // queue[stall_name])
        ppl_str = str(minute)

        # create a label to show the queuing time message
        show_var = 'Estimated queuing time is: ' + ppl_str + ' minutes'
        canvas.create_text(data.width // 2, data.height * 2 // 3 - 20, text=show_var, font='Arial 35')

    # entering message
    canvas.create_text(data.width // 2, data.height // 3 + 40, text='Please enter the number of pax queuing:'
                       , font='Arial 35')

    # the entry for the number of queuing people
    queue_enter = Entry(root, font='Arial 30', width=15)
    queue_enter.place(x=data.width // 2 - 70, y=data.height // 2 + 10, anchor=CENTER)

    # a button for calculate the time
    calculate_btn = Button(root, text='Calculate', width=9, height=2, command=show_queue_time, font='Arial 19')
    calculate_btn.place(x=data.width // 2 + 115, y=data.height // 2 + 10, anchor=CENTER)


def operating_hours(root, data, stall_name):
    canvas = display_stall(root, data, stall_name)

    # read operating hour
    filename = stall_name + ' op'
    info_list_op = get_info(filename)

    # display operating hour
    for i, word in enumerate(info_list_op):
        canvas.create_text((data.width // 2, 410), text=word, anchor=CENTER, font='Arial 45')
