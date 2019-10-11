import random
doors = [1, 2, 3] 
choice = 0 #Variable to hold the door the contestant picks initially
car_door = 0 #Variable to hold the door containing the car
opened_door = 0 #Variable to hold the door the host opens, to reveal a goat
change = True #Does the contestant change his door, after the host opens one?
change_and_win = 0 #How often does the contestant change the door, and win?
change_and_lose = 0 #How often does the contestand change the door, and lose?
for i in range(10000): 
	car_door = random.choice(doors) 
	choice = random.choice(doors) 
	opened_door = random.choice([element for element in doors if element != car_door and element != choice]) 
	change = random.choice([True, False]) 
	if car_door == choice: #If contestant's initial door has the car
		change_and_lose = change_and_lose + 1 #If he changes the door, he loses
	else: #If contestant's initial door does not have the car: 
		change_and_win = change_and_win + 1 #If contestant changes the door, he wins, as both his initial choice, and the opened door, do not have the car
print "Number of times you change your door, and win: ", change_and_win
print "Number of times you change your door, and lose: ", change_and_lose