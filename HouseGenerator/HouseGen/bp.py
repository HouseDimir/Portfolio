import os
import gen
import sys
import tkinter as tk

print(os.getcwd())

run = True
while run:
    try:
        num_of_floors = int(input('Please enter the number of floors you want:'))
        run = False
    except ValueError:
        print('That was not an integer, please try again.')

house = []
floor = []
room = {}
house_gen = gen.Get_House_Layout(num_of_floors)
house.append(house_gen)

def PrintRoom(house):
    for floor in house:
        for room in floor:
            for room in room:
                room_type = ('Master Bedroom', 'Master Bathroom', 'Bedroom 1',
                'Bedroom 2', 'Bathroom 1', 'Bathroom 2', 'Living room',
                'Kitchen')
                for value in room_type:
                    if value in room.values():
                        print(value)
                    else:
                        pass
            print('\n')

PrintRoom(house)