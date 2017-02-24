#number of vehicles
vehicle_count = 2

#define directions, movement and commands
directions = ['N','E','S','W'] 
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}

#add u_turn as test
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move', 'LU':'left_uturn', 'RU':'right_uturn'}

#Vehicle class 
class Vehicle():
    def __init__(self, x, y, max_x, max_y, face, occupied_cells):
	  self.x = x
	  self.y = y
	  self.max_x = max_x
	  self.max_y = max_y
	  self.face = face
	  self.occupied_cells = set(occupied_cells)

    def turn_left(self):
	  self.face = directions[(directions.index(self.face)-1) % len(directions)]

    def turn_right(self):
	  self.face = directions[(directions.index(self.face)+1) % len(directions)]
    
    # need further work
	def left_uturn(self):
	  self.face = directions[(directions.index(self.face)-2) % len(directions)]
	
    #need further work
    def right_uturn(self):
	  self.face = directions[(directions.index(self.face)+2) % len(directions)]

    def move(self):
	  new_x = self.x + movement[self.face][0]
	  new_y = self.y + movement[self.face][1]
      
      #check if the vehicle within the grid  
	  if (new_x,new_y) not in self.occupied_cells:
		  if new_x <= self.max_x:
			  self.x = new_x
		  if new_y <= self.max_y:
			  self.y = new_y

if __name__ == '__main__':
  
  #starting point X Y on the grid
  max_x, max_y = map(int, raw_input().split())

  occupied_cells = set([])
  results = []

  for _ in range(vehicle_count):
	x,y,face  = raw_input().split()
	
	vehicle = Vehicle(int(x), int(y), max_x, max_y, face, occupied_cells)
	for command in raw_input():
	  getattr(vehicle, commands[command])()
	
	occupied_cells.add((vehicle.x, vehicle.y))
	results.append((vehicle.x, vehicle.y, vehicle.face))

  for result in results:
	print result
