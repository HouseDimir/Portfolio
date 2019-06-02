import os
import gen
import sys
import tkinter as tk

master = tk.Tk()
def MainLoop():
    '''Accesses and returns the Tkinter mainloop function'''
    return tk.mainloop()

def Message(text):
    '''Sets the default config for messages displayed by the program
        and initializes the message.'''
    msg = tk.Message(master, text=text)
    msg.config()
    msg.pack()

print(os.getcwd())

run = True
while run:
    try:
        num_of_floors = int(input('Please enter the number of floors you want:'))
        run = False
    except ValueError:
        print('That was not an integer, please try again.')
        # x = False
        # if not x:
        #     error = "That was not an integer, please try again."
        #     Message(error)
        #     MainLoop()
        # else:
        #     pass

house = []
floor = []
room = {}
house_gen = gen.Get_House_Layout(num_of_floors)
house.append(house_gen)

class BluePrint(tk.Canvas):
    '''BluePrint class to draw and customize the floor plan for the house.'''
    def __init__(self, master):
        '''Construct the BluePrint instance with a Window name of BluePrint
        a fixed size of 1080x720,  and a master of tk.Tk()'''
        self.window_name = 'BluePrint'
        self.size = '1080', '720'
        self.master = master
        # Eventually bind a function to keybind <Alt-A>
        # in order to build the canvas, pass the values
        # and draw out the floor plan. this will likely 
        # look like the following code:
        # tk.canvas.bind(sequence='<Alt-A-ButtonRelease-ButtonRelease>', func=DrawCanvas(value))

    def Draw_Room(house):
        # Builds the floor plan of the house room by room, with space 
        # between each floor.
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

BluePrint(master)
print(BluePrint(master).window_name)
BluePrint(master).Draw_Room(house)