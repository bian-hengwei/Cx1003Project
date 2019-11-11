"""
CX1003 Introduction to Computational Thinking Mini Project
Real-time Canteen Information System
FS1 Bian Hengwei
FS1 Bryan Lim
FS1 Cheng Yu Feng
Console user interface
Used to test all inner functions
"""


from Canteen_Info_Sys import *


def cover():

    print('''
    Nanyang Technological University
    North Spine Canteen Information System
    Press Enter To Display All Stall Names
    Or q to Quit
    ''')

    enter = input()
    while True:
        if enter == '':
            break
        elif enter == 'q':
            return
        enter = input()

    print('Stalls:')

    stalls_list = get_stalls()
    if isinstance(stalls_list, str):
        print(stalls_list)

    else:
        stalls_count = 0
        for stall_name in stalls_list:
            print(stalls_count + 1, '. ', stall_name)
            stalls_count += 1
        select_stall(stalls_list)


def select_stall(stalls_list):

    print('''
    Enter the Stall Index to View Stall Information
    ''')

    stall_index = input()
    while True:
        if stall_index.isdigit() and int(stall_index) - 1 in range(len(stalls_list)):
            stall_name = stalls_list[int(stall_index) - 1]
            break
        print('Invalid Input')
        stall_index = input()

    display_stall(stall_name)


def display_stall(stall_name):

    operating_hour, menu = get_info(stall_name)

    print(operating_hour)
    print()

    print('MENU:')
    for dish in menu:
        print(dish)


def main():
    cover()


if __name__ == '__main__':
    main()
