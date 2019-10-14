"""
CX1003 Introduction to Computational Thinking Mini Project
Real-time Canteen Information System
FS1 Bian Hengwei
FS1 Bryan Lim
FS1 Cheng Yu Feng
Basic algorithms that reads txt files and user inputs
to meets the project objectives
"""


# returns the stalls list stored in stalls_list.txt
def get_stalls():

    # opens the stalls list
    # prints an error message if the file is not found
    try:
        stalls_list_file = open('stalls_list.txt', 'rt')
    except FileNotFoundError:
        return 'Cannot find the stores list'

    # reads the file and convert it into a list object
    # returns the list
    stalls_list_text = stalls_list_file.read()
    stalls_list = stalls_list_text.splitlines()
    return stalls_list


# return the information of a specific store
def get_info(store_name):

    # opens the info file
    # prints an error message if the file is not found
    try:
        info_file = open(store_name + '.txt', 'rt')
    except FileNotFoundError:
        return 'Cannot find the info file'

    # reads the file and convert it into a list object
    # returns the list
    info_text = info_file.read()
    info_list = info_text.splitlines()

    # info_list[0] is the operation hours
    # info_list[1:] is the menu
    # return a tuple of the above mentioned information
    return info_list[0], info_list[1:]


# according the input time
# returns the available menu
def get_current_menu(menu_list, current_time):
    pass
