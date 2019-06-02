import random as rand

'''This module generates the necessary variables for the blueprint to
be drawn.'''

house = []
room_type = ('Master Bedroom', 'Master Bathroom', 'Bedroom 1',
			'Bedroom 2', 'Bathroom 1', 'Bathroom 2', 'Living room',
			'Kitchen')

if __name__ == '__main__':
	run = True
	while run:
		try:
			num_of_floors = int(input('Please enter the number of floors you want:'))
			run = False
		except ValueError:
			print('That was not an integer, please try again.')
else:
	pass

def Generate_Room(num_of_rooms):
	'''Generates a variable number of randomized rooms.'''
	for i in range(num_of_rooms):
		room = {}
		room['room_type'] = rand.choice(room_type)
		yield room

def Generate_Floor(num_of_floors):
	'''Appends a given number of rooms to that floor, plus a set
	   of stairs.'''
	for i in range(num_of_floors):
		floor = []
		stairs = {'room_type':'Stairs'}
		run = True
		while run == True:
			try:
				num_of_rooms = int(input('Please enter the number of rooms you want:'))
				run = False
			except ValueError:
				print('That was not an integer, please try again.')
		for i in range(num_of_rooms):
			room = next(Generate_Room(num_of_rooms))
			floor.append(room)
		floor.append(stairs)
		yield floor

if __name__ == '__main__':
	for i in range(num_of_floors):
		floor = next(Generate_Floor(num_of_floors))
		house.append(floor)

	for floor_number, floor in enumerate(house):
		print('Floor', floor_number + 1, ': ', sep='', end=' ')
		for room in floor:
			if room['room_type'] == 'Stairs':
				print(room['room_type'])
			else:
				print(room['room_type'], end=', ')
else:
	def Get_House_Layout(num_of_floors):
		for i in range(num_of_floors):
			floor = next(Generate_Floor(num_of_floors))
			house.append(floor)
		return house