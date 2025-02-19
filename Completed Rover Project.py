class Rover(): # Ended being more of a storage for where rovers where placed around the plateau
    def __init__(self): 
        self.Occupied_Locations = [] #This list holds the various locations of rovers that have sucessfully moved to another location, to later be used to check for possible rover collisions

    def Occupying(self,Rover_Occupy):
        self.Occupied_Locations.append(Rover_Occupy)
  # Current position and direction are all user input

class Plateau ():
    def __init__(self, Angle, Rover_X, Rover_Y): # Gonna pass self.Direction from rover into Angle
        self.Position_Angle = Angle
        self.New_positionX = int(Rover_X) #Both Newposition variables are constantly changing until they reach their final destination
        self.New_positionY = int(Rover_Y)
        self.Error_Occured = False #Boolean value to determine whether a Rover has made a 'legal' move or not
        self.Taken_Space = getattr(Drone,'Occupied_Locations') #Pulls the list of occupied rover locations from the rover class

    #Explanation for this Plateau creation:
    #Essentially changing the way i think about it a bit essentialyl the max x value acts as the max amount of values that inside 1 sub list where as the
    # The Max Y value acts as the max amount of sub list there can be and in that way i have my own kind of grid
    # If you picture this in a square form it looks a lot more like a grid and the y acts as the rows going down or up

    def Plateau_Create(self, Max_X, Max_Y): #When the user input their upper right coords then they will be seperated into the max y coordinate and the max x axis respectively
        Inner_List = [] 
        for i in range(Max_X + 1 ): #Had to increase by 1 to account for the fact a grid starts at (0,0) rather than 1 so in order to reach the user's actual grid size it must be increased by 1v 
            Inner_List.append("") 
        Outer_List = []
        for i in range(Max_Y + 1):
            Outer_List.append(list(Inner_List))
        
        self.Max_X = Max_X
        self.Max_Y = Max_Y

    def Positiion_Check(self): # The only conditions i thought at the time had any relevance in checking before a position was confirmed
        Current_Position = (self.New_positionX, self.New_positionY)

        if self.New_positionX > self.Max_X or self.New_positionX < 0:
            print("This move cannot be made as it goes outside the bounds of your plateau!! ")
            self.Error_Occured = True
            
        if self.New_positionY > self.Max_Y or self.New_positionY < 0:
             print("This move cannot be made as it goes outside the bounds of your plateau!! ")
             self.Error_Occured = True

        if Current_Position in self.Taken_Space:
            print("This move is not possible as there is already a rover in this position")
            self.Error_Occured = True
           

    def DirectiontoAngle(self): #Converts the user's intial direction into values that represent angles, that i will later to use to determine how the rover moving will have an effect on the x or y axis 
        if self.Position_Angle == 'N' or self.Position_Angle == 'n':
            self.Position_Angle = 0  
        
        elif self.Position_Angle == 'E' or self.Position_Angle == 'e':
            self.Position_Angle = 90

        elif self.Position_Angle == 'S'or self.Position_Angle == 's':
            self.Position_Angle = 180

        elif self.Position_Angle == 'W'or self.Position_Angle == 'w':
            self.Position_Angle = 270
    
    def Direction_Change(self,Turn_Action): #Reasoning for the 2 if statements per right and left is that if you imagine a traditional 4-way compass but instead with angles, once a full cycle is completed 
        #There would be incorrect values if i don't reset the values e.g if turn right after 270, i can't use 360 to check if it is still north as it have it set at 0 so it's less time and effort wasted on accounting for every possible values of north or south for example
        if Turn_Action == 'R'and self.Position_Angle != 270:
            self.Position_Angle += 90

        elif Turn_Action == 'R'and self.Position_Angle == 270: # Essentially if Angle is West and user wish to turn right instead of being 360 it resets back to 0, thus acting as north again
            self.Position_Angle = 0

        if Turn_Action == 'L' and self.Position_Angle != 0:
            self.Position_Angle -= 90

        elif Turn_Action == 'L' and self.Position_Angle == 0:
            self.Position_Angle = 270

    def Movement(self): #Based on the angle it moves it up, down, left or right on the grid by subracting or adding on either the x axis or y-axis
        if self.Position_Angle == 0:
            self.New_positionY += 1

        if self.Position_Angle == 90:
            self.New_positionX += 1

        if self.Position_Angle == 180:
            self.New_positionY -= 1

        if self.Position_Angle == 270:
            self.New_positionX -= 1

Rover_Num = int(input("How many Rovers will you be keeping track of on the Plateau in integer form: ")) # For now only 1 will be accepted until i get the rest of it working
Max_Xsize = input("What are the upper right x-coordinate of your Plateau: ")
Max_Ysize = input("What are the upper right y-coordinate of your Plateau: ")

Drone = Rover()

for Number in range(Rover_Num):
    Start_PositionX = input("What is the starting X axis position of your rover: ") 
    Start_PositionY = input("What is the starting Y axis position of your rover: ")
    Start_Direction = input("What is the starting direction of your rover (N, E, S, W): ")

    Commands = input("How would you like for your Rover to move throughout the plateau keep in mind L = Turn Left, R = Turn Right and M = Move by 1 space and please enter without any spaces between characters: ") #Create a condition that once a space is found between a command the entire command is rejected and they are asked to try again

    Grid = Plateau(Start_Direction, Start_PositionX, Start_PositionY)
    Grid.Plateau_Create(int(Max_Xsize), int(Max_Ysize))
    Grid.DirectiontoAngle()
    Rover_Completed = False

    while Rover_Completed != True and Number != Rover_Num : # Keeps the user stuck in this while loop until they enter a suitable command and until they have reached their supposed amount of rovers placed on the Plateau
        for i in Commands:  
            if i == "L":
                Grid.Direction_Change(i)
            if i == "R":
                Grid.Direction_Change(i)
            if i == "M":
                Grid.Movement()
        Grid.Positiion_Check()
        Rover_Position = (Grid.New_positionX, Grid.New_positionY) 

        if Grid.Error_Occured == False:
            print("Rover ", Number + 1," has completed its journey at ", Rover_Position) 
            Rover_Completed = True
            Drone.Occupying(Rover_Position)

        else: 
            Commands = input("Please issue a new command instead: ")
            Grid = Plateau(Start_Direction, Start_PositionX, Start_PositionY) #Just takes the same information as before and when the while loop starts gaing it should run as planned
            Grid.Plateau_Create(int(Max_Xsize), int(Max_Ysize))
            Grid.DirectiontoAngle()

print("These are the final coordinates for your squad of Rovers:", Drone.Occupied_Locations)
            
        
