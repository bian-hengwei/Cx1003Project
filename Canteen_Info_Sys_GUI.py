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

from time import *


# initializes data that MUST be initialized in the main() function
def initialize(data):
    data.cover = PhotoImage(file='images/cover.png')
    data.Cantonese = PhotoImage(file='images/Cantonese.png')
    data.Japanese = PhotoImage(file='images/Japanese Korean Delight.png')
    data.Malay = PhotoImage(file='images/Malay BBQ.png')
    data.McDonald = PhotoImage(file='images/McDonald\'s.png')
    data.Sandwich = PhotoImage(file='images/The Sandwich Guys.png')
    data.Vietnamese = PhotoImage(file='images/Vietnamese Cuisine.png')

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
                                 command=lambda: change_date(root, data))
    select_stall_button.place(x=data.width * 3 // 4, y=data.height // 3 - 20,
                              width=300, height=120, anchor=CENTER)

    # exit button
    Button(canvas, text='Exit', font='Times 30 bold',
           command=root.destroy).place(x=data.width * 3 // 4,
                                       y=data.height * 2 // 3 - 20, width=300, height=120, anchor=CENTER)

    draw_change_date(root, canvas, data)


# draws change date buttons and drop_down lists on cover
def draw_change_date(root, canvas, data):
    # a constant for drop-down list
    margin = 55

    # date drop-down list
    dates_list = ['0' + str(x) for x in range(1, 10)] + [str(x) for x in range(10, 32)]

    date_variable = StringVar(root)
    date_variable.set(data.time.to_string()[5:7])  # default value

    date_drop_down_list = OptionMenu(root, date_variable, *dates_list)
    date_drop_down_list.place(x=605, y=data.height // 2 - 7, width=margin, anchor=SW)

    # month drop-down list
    months_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    month_variable = StringVar(root)
    month_variable.set(data.time.to_string()[8:11])  # default value

    month_drop_down_list = OptionMenu(root, month_variable, *months_list)
    month_drop_down_list.place(x=605 + margin, y=data.height // 2 - 7, width=margin, anchor=SW)

    # year drop-down list
    years_list = [x for x in range(2000, 2030)]

    year_variable = StringVar(root)
    year_variable.set(data.time.to_string()[12:16])  # default value

    year_drop_down_list = OptionMenu(root, year_variable, *years_list)
    year_drop_down_list.place(x=605 + 2 * margin, y=data.height // 2 - 7, width=margin + 15, anchor=SW)

    # hour drop-down list
    hours_list = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'] + [str(x) for x in range(10, 24)]

    hour_variable = StringVar(root)
    hour_variable.set(data.time.to_string()[18:20])  # default value

    hour_drop_down_list = OptionMenu(root, hour_variable, *hours_list)
    hour_drop_down_list.place(x=605 + 3 * margin + 15, y=data.height // 2 - 7, width=margin, anchor=SW)

    # minute drop-down list
    minutes_list = ['0' + str(x) for x in range(10)] + [str(x) for x in range(10, 60)]

    minute_variable = StringVar(root)
    minute_variable.set(data.time.get_current_time().to_string()[21:23])  # default value

    minute_drop_down_list = OptionMenu(root, minute_variable, *minutes_list)
    minute_drop_down_list.place(x=605 + 4 * margin + 15, y=data.height // 2 - 7, width=margin, anchor=SW)

    # get all the above drop-down list value
    def get_var():
        date_str = date_variable.get()
        month_str = month_variable.get()
        year_str = year_variable.get()
        hour_str = hour_variable.get()
        minute_str = minute_variable.get()
        new_time = date_str, month_str, year_str, hour_str, minute_str
        change_date(root, data, new_time)

    # Change date button
    change_date_button = Button(canvas, font='Times 30 bold', text="VIEW STORE BY:\n\nEnter",
                                command=get_var)
    change_date_button.place(x=data.width * 3 // 4, y=data.height // 2 - 20, width=300, height=120, anchor=CENTER)


# changes current date
def change_date(root, data, new_time='reset'):
    data.time.change_date(new_time)
    select_stall(root, data)


# pops up an error page
def error_page(error_message='Unexpected Error'):
    window = Tk()
    window.title('ERROR')
    window.geometry('300x70')
    error_label = Label(window, text=error_message)
    error_label.pack()


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
    stalls_list = get_stalls(data)
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


# display the basic stall window
# called by specific stall functions
def display_stall(root, data, stall_name):
    # clears the root
    for canvas in root.winfo_children():
        canvas.destroy()

    # creates a new canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(highlightthickness=0)
    canvas.pack()

    # give a background for each store
    stalls_list = get_stalls(data)
    x = stalls_list.index(stall_name)
    image_dic = {0: data.McDonald, 1: data.Sandwich, 2: data.Japanese, 3: data.Cantonese, 4: data.Malay,
                 5: data.Vietnamese}
    canvas.create_image(data.width // 2, data.height // 2, image=image_dic[x])

    # menu button
    menu_button = Button(canvas, text='Menu', font='Times 20', command=lambda: menu(root, data, stall_name))
    menu_button.place(x=data.width // 3, y=data.height // 15 + 30, width=data.width // 10,
                      height=data.height // 15, anchor=CENTER)
    # queue time button
    queue_time_button = Button(canvas, text='Queue\nTime', font='Times 20',
                               command=lambda: queue_time(root, data, stall_name))
    queue_time_button.place(x=data.width // 2, y=data.height // 15 + 30, width=data.width // 10,
                            height=data.height // 15, anchor=CENTER)
    # operating hours button
    operating_hours_button = Button(canvas, text='Operating\nHours',
                                    font='Times 20', command=lambda: operating_hours(root, data, stall_name))
    operating_hours_button.place(x=data.width * 2 // 3, y=data.height // 15 + 30, width=data.width // 10,
                                 height=data.height // 15, anchor=CENTER)

    # stall name
    canvas.create_text(data.width // 2, data.height // 7 + 50, text=stall_name, font='Impact 60', fill='white')

    # a back button
    back_button = Button(canvas, text='BACK', font='Times 30 bold', command=lambda: select_stall(root, data))
    back_button.place(x=0, y=data.height, width=100, height=80, anchor=SW)

    return canvas


# display the menu of a specific stall
def menu(root, data, stall_name):
    # draws the shared stall window
    canvas = display_stall(root, data, stall_name)

    # reads the stalls info
    info_list = get_info(stall_name)[1]

    # prints stalls menu
    x_base, y_base, margin = 220, 270, 50
    for i, word in enumerate(info_list):
        canvas.create_text((x_base, y_base + i * margin), text=word, anchor=W, font='Bookman 30',
                           fill='white')


def queue_time(root, data, stall_name):

    # draws the shared window
    canvas = display_stall(root, data, stall_name)

    # function for showing queue time
    def show_queue_time():

        canvas.delete('queue_time')

        # get the value from the entry below
        queue_length = queue_enter.get()

        # the waiting time for each store per person
        queues = {"McDonald's": 0.4, "The Sandwich Guys": 1.5, "Japanese Korean Delight": 1.1,
                  "Vietnamese Cuisine": 1.4, "Malay BBQ": 1.25, "Cantonese Roast Duck": 0.8}

        try:

            # calculate the queue time
            queue = int(queue_length)

            assert 0 <= queue < 100
            waiting_time = str(int(queue // queues[stall_name]))
            # create a label to show the queuing time message
            show_var = 'Estimated queuing time is: ' + waiting_time + ' minutes'
            canvas.create_text(data.width // 2, data.height * 2 // 3 - 20, text=show_var, font='Arial 35',
                               fill='white', tag='queue_time')

        # if the user input is not valid
        except AssertionError:

            # create a pop up window for error message
            error_page('Queue Length Should Be Between 1 and 99!')

        except ValueError:

            # create a pop up window for error message
            error_page('Please Enter An Integer')

    # entering message
    canvas.create_text(data.width // 2, data.height // 3 + 40, text='Please Enter The Number of Pax Queuing:'
                       , font='Arial 35', fill='white')

    # the entry for the number of queuing people
    queue_enter = Entry(root, font='Arial 30', width=15)
    queue_enter.place(x=data.width // 2 - 70, y=data.height // 2 + 10, anchor=CENTER)

    # a button for calculate the time
    calculate_btn = Button(root, text='Calculate', width=9, height=2, command=lambda: show_queue_time(),
                           font='Arial 19')
    calculate_btn.place(x=data.width // 2 + 115, y=data.height // 2 + 10, anchor=CENTER)


def operating_hours(root, data, stall_name):
    canvas = display_stall(root, data, stall_name)

    # read operating hour
    filename = stall_name + ' op'
    info_list_op = get_info(filename)

    # display operating hour
    for i, word in enumerate(info_list_op):
        canvas.create_text((data.width // 2, 410), text=word, anchor=CENTER, font='Arial 45', fill='white')
