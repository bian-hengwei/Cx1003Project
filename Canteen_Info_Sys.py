"""
CX1003 Introduction to Computational Thinking Mini Project
Real-time Canteen Information System
FS1 Bian Hengwei
FS1 Bryan Lim
FS1 Cheng Yu Feng
Basic algorithms that reads txt files and user inputs
to meet the project objectives
"""

from datetime import *


# returns the stalls list stored in stalls_list.txt
def get_stalls():
    # opens the stalls list
    # prints an error message if the file is not found
    try:
        stalls_list_file = open('data/stalls_list.txt', 'rt')
    except FileNotFoundError:
        return 'Cannot find the stalls list'

    # reads the file and convert it into a list object
    # returns the list
    stalls_list_text = stalls_list_file.read()
    stalls_list = stalls_list_text.splitlines()
    return stalls_list


# return the information of a specific store
def get_info(stall_name):
    # opens the info file
    # prints an error message if the file is not found
    try:
        filename = 'data/' + stall_name + '.txt'
        info_file = open(filename, 'rt')
    except FileNotFoundError:
        return 'Cannot find the info file'

    # reads the file and convert it into a list object
    # returns the list
    info_text = info_file.read()
    info_list = info_text.splitlines()

    # info_list[0] is the operating hours
    # info_list[1:] is the menu
    # return a tuple of the above mentioned information

    return info_list[0], info_list[1:]


# according the input time
# returns the available menu
def get_current_menu(menu_list, current_time):
    pass


# class Time that records the time
class Time:

    # initialize an empty Time object
    def __init__(self):
        self.day_of_week = None
        self.date = None
        self.month = None
        self.year = None
        self.hour = None
        self.minute = None
        self.months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # set the time instances to current time value
    def get_current_time(self):
        self.day_of_week = datetime.now().weekday()
        self.date = datetime.now().strftime('%d')
        self.month = datetime.now().strftime('%m')
        self.year = datetime.now().strftime('%Y')
        self.hour = datetime.now().strftime('%H')
        self.minute = datetime.now().strftime('%M')
        return self

    # return a string representation of any Time object
    def to_string(self):
        time_string = ''

        time_string += self.days_of_week[self.day_of_week] + ', '
        time_string += self.date + ' ' + self.months[int(self.month)]
        time_string += ' ' + self.year + ', ' + self.hour + ':' + self.minute

        return time_string

    def change_date(self, time_string):
        self.date = time_string[0:2]
        self.month = str(self.months.index(time_string[3:6]))
        self.year = time_string[7:11]
        self.hour = time_string[13:15]
        self.minute = time_string[16:]
        self.day_of_week = datetime(int(self.year), int(self.month), int(self.date)).weekday()
