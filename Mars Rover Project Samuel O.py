class Rover:
    def __init__(self, Start_y,Start_x,Grid_Limit,Next_input):
        self.Next_input = Next_input
        self.Start_x = int(Start_x)
        self.Start_y = int(Start_y)
        self.Bearing = "N" 
        self.Grid_Limit = str(Grid_Limit)
        self.Bearing_val = 360

    def grid(self): # Could add base x as a attribute and mention how it increases in when things move
        comma = self.Grid_Limit.find(",")
        X_Limit = self.Grid_Limit[:comma]
        Y_Limit = self.Grid_Limit[comma+1:]
        global grid 
        grid = [[0 for i in range(int(Y_Limit))] for j in range(int(X_Limit))] # - Currently wrong its producing between these values rather than, im gonna have to look at the internet for a solution
        grid[self.Start_y][self.Start_x] = 1 #puts the rover's starting position with a value of 1 in the array
        for i in grid:
            for j in i:
                if j > 0:
                    print("There is a rover in this position", j,i )
                    global Taken_position
                    Taken_position = [j,i]



    def Move(self):
         for i in self.Next_input:
             if i == "L":
                 self.Bearing_val =  -abs(self.Bearing_val) + 90 # Makes the value of bearing negative only way to make the left command work this way
                 self.Bearing_val = abs(self.Bearing_val)
                 if self.Bearing_val == 360:
                     self.Bearing = "N"
                 elif self.Bearing_val == 270:
                     self.Bearing = "W"
                 elif self.Bearing_val == 180:
                     self.Bearing = "S"
                 elif self.Bearing_val == 90:
                     self.Bearing = "E"
                 elif self.Bearing_val == 0:
                     self.Bearing = "N"
                     self.Bearing_val = 360
                 
             if i == "M":
                
                if self.Bearing == "N":
                    grid[self.Start_y][self.Start_x] = 0
                    self.Start_y = self.Start_y + 1
                if self.Bearing == "E":
                    grid[self.Start_y][self.Start_x] = 0
                    self.Start_x = self.Start_x - 1
                if self.Bearing == "S":
                    grid[self.Start_y][self.Start_x] = 0
                    self.Start_y = self.Start_y - 1
                if self.Bearing == "W":
                    grid[self.Start_y][self.Start_x] = 0 #Ensure previous position marked with value 1 is replaced with a 0 to highlight the rover is no longer there
                    self.Start_x = self.Start_x + 1

                global New_Position
                New_Position = [self.Start_y, self.Start_x] #Rover's moved position
                if New_Position == Taken_position:
                    New_Position = [self.Start_y - 1, self.Start_x - 1]
                    print("This position is already taken so we have moved it 1 position away on the x and y axis")
                
             if i == "R":
                self.Bearing_val = self.Bearing_val - 90
                if self.Bearing_val == 360:
                    self.Bearing = "N"
                elif self.Bearing_val == 270:
                    self.Bearing = "E"
                elif self.Bearing_val == 180:
                    self.Bearing = "S"
                elif self.Bearing_val == 90:
                    self.Bearing = "W"
                elif self.Bearing_val == 0:
                     self.Bearing = "N"
                     self.Bearing_val = 360
            
         global Increment_val # Whole point of this is every new rover is marked in a different spot with a different number in order to differentiate them
         Increment_val = 0
         Increment_val = Increment_val + 1 
         

    def Change_Position(self):
        global Position_given
        Position_given = False
        while Position_given == False:
            grid[New_Position[0]][New_Position[1]] = Increment_val
            Position_given = True 

    def Give_Position(self):
        global Direction
        Direction = self.Bearing
        print("Your Rover's new position is", New_Position[0], New_Position[1], Direction)
        
Rover_amount = int(input("How many Rovers are planning to move: "))
if Rover_amount == " ":
    print("Please add a valid amount of Rovers you want to place on your grid and try again")
    quit()

for i in range(Rover_amount):
    Xposition = input("What row of your grid does your rover start on: ")
    Yposition = input("What column of your grid does the rover start on?: ")
    Limit = input("What are the uppper right coordinates for your grid: ")
    User_input = input ("How would you like your rover to move and at what bearing: ")
    if Xposition or Yposition or Limit or User_input == " ":
        print("Please enter a valid input and try again ")
        quit()

    New_Rover = Rover(Xposition, Yposition, Limit, User_input)
    New_Rover.grid()
    New_Rover.Move()
    New_Rover.Change_Position()
    New_Rover.Give_Position()


#Take an input of the rovers's position
#Have the code be able to see what the next command is accordingly
#M should + or - the values of x or y by the amount moved 
#Depending what direction is selected
#If bearing is sourth or north it will affect the y-axis 
# The values of the bearings will then be multiplied by the amount moved added to their corresponding axis
# The final destination of the rover is then given


