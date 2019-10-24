"""
CX1003 Introduction to Computational Thinking Mini Project
Real-time Canteen Information System
FS1 Bian Hengwei
FS1 Bryan Lim
FS1 Cheng Yu Feng
Basic algorithms that reads txt files and user inputs
to meets the project objectives
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


class Time(object):

    def __init__(self):
        self.day_of_week = None
        self.date = None
        self.month = None
        self.year = None
        self.hour = None
        self.minute = None

    def get_current_time(self):
        self.day_of_week = datetime.now().weekday()
        self.date = int(datetime.now().strftime('%d'))
        self.month = int(datetime.now().strftime('%m'))
        self.year = int(datetime.now().strftime('%Y'))
        self.hour = int(datetime.now().strftime('%H'))
        self.minute = int(datetime.now().strftime('%M'))

    def to_string(self):
        time_string = ''

        time_string += '{0}, {1} {2}'.format(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][self.day_of_week],
                                             str(self.date),
                                             ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                                              'Nov', 'Dec'][self.month])
        time_string += ' ' + str(self.year) + ', ' + str(self.hour) + ':' + str(self.minute)

        return time_string
