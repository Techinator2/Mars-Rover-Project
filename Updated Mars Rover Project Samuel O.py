class Rover:
    def __init__(self, Start_y,Start_x,Next_input,Grid_Limit):
        self.Start_x = int(Start_x)
        self.Start_y = int(Start_y)
        self.Next_input = Next_input
        self.Bearing = "N" 
        self.Bearing_val = 360
        self.Grid_Limit = str(Grid_Limit)

    def Move(self):
         Grid1 = Grid_Manager
         Grid_Val = Grid1.grid(self)
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
                    Grid_Val[self.Start_y][self.Start_x] = 0
                    self.Start_y = self.Start_y + 1
                if self.Bearing == "E":
                    Grid_Val[self.Start_y][self.Start_x] = 0
                    self.Start_x = self.Start_x - 1
                if self.Bearing == "S":
                    Grid_Val[self.Start_y][self.Start_x] = 0
                    self.Start_y = self.Start_y - 1
                if self.Bearing == "W":
                    Grid_Val[self.Start_y][self.Start_x] = 0 #Ensure previous position marked with value 1 is replaced with a 0 to highlight the rover is no longer there
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
         return New_Position

class Grid_Manager:
    def __init__(self, Start_x,Start_y,Grid_Limit):
        self.Start_x = Start_x
        self.Start_y = Start_y
        self.Grid_Limit = str(Grid_Limit)

    def grid(self): # Could add base x as a attribute and mention how it increases in when things move
        comma = self.Grid_Limit.find(",")
        X_Limit = self.Grid_Limit[:comma]
        Y_Limit = self.Grid_Limit[comma+1:]
        grid = [[0 for i in range(int(Y_Limit))] for j in range(int(X_Limit))] # - Currently wrong its producing between these values rather than, im gonna have to look at the internet for a solution
        grid[self.Start_y][self.Start_x] = 1 #puts the rover's starting position with a value of 1 in the array
        for i in grid:
            for j in i:
                if j > 0:
                    print("There is a rover in this position", j,i )
                    global Taken_position # For some reason i can't get the variable below to actually function without making it global
                    Taken_position = [j,i]
        self.Grid_val = grid 
        return self.Grid_val
    
    def Change_Position(self,Grid_Val):
        self.Grid_val = Grid_Val
        
        Position_given = False
        Increment_val = 0
        while Position_given == False:
            self.Grid_val[New_Position[0]][New_Position[1]] = Increment_val
            Increment_val = Increment_val + 1 
            Position_given = True 

    def Give_Position(self,Direct):
        Direction = Direct 
        print("Your Rover's new position is", New_Position[0], New_Position[1], Direction)


Rover_amount = int(input("How many Rovers are planning to move: "))
if Rover_amount == " ":
    print("Please add a valid amount of Rovers you want to place on your grid and try again")
    quit()

for i in range(Rover_amount):
    Xposition = input("What row of your grid does your rover start on: ")
    Yposition = input("What column of your grid does the rover start on?: ")
    Limit = input("What are the uppper right coordinates for your grid in the form a,b: ")
    User_input = input ("Enter your commands (L - Turn Left, R - Turn Right, M - Move ): ")
    if Xposition == " " or Yposition == " " or Limit == " " or User_input == " ":
        print("Please enter a valid input and try again ")
        quit()

    New_Rover = Rover(Xposition,Yposition,User_input,Limit) 
    Plateau = Grid_Manager(New_Rover.Start_x, New_Rover.Start_y, Limit)
    New_Rover.Move()
    Plateau.grid()
    Plateau.Change_Position(Plateau.Grid_val)
    Plateau.Give_Position(New_Rover.Bearing)


#Take an input of the rovers's position
#Have the code be able to see what the next command is accordingly
#M should + or - the values of x or y by the amount moved 
#Depending what direction is selected
#If bearing is sourth or north it will affect the y-axis 
# The values of the bearings will then be multiplied by the amount moved added to their corresponding axis
# The final destination of the rover is then given


