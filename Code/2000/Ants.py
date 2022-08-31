#Solution made by @Catatria
print("Co-ordinates are from 1 - 11")
print("Directions are T  = Top, B = Bottom, L = Left, R = Right")
print("Please use the format 'x y d' e.g. '1 1 T'\n") # Makes sure user knows what to input
position1 = str(input("Input ant 1's co-ordinates and direction: "))
position2 = str(input("Input ant 2's co-ordinates and direction: ")) # Prompts user for input

info1 = position1.split(" ")
info2 = position2.split(" ") # Creates list where each item is seperated, rather than being in one long string


class Ant: # Creates a class called ant
    def __init__(self, x, y, direction): # Assigning values to object properties
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, x, y, direction):
        if x <= 0 or x >= 12 or y <= 0 or y >= 12:
            self.x = 99 # Moves ant outside of grid when already outside, makes sure an ant doesn't get back in the grid (probably not necessary ¯\_(ツ)_/¯)
        else:
            if direction == "T":
                y += 1
            elif direction == "R":
                x += 1
            elif direction == "B":
                y -= 1
            elif direction == "L": # Changes position in grid
                x -= 1
            if x <= 0 or x >= 12 or y <= 0 or y >= 12: # Again, checks if ant is outside the grid and sends them far away
                self.x = 99
            else:
                grid_x = x - 1
                grid_y = -y + 11 # Changing the co-ordinates to suit the 2d array (normal co-ordinates start at 1, list co-ordinates start at 0)
                if grid[grid_y][grid_x] == ".":
                    grid[grid_y][grid_x] = "*" # Checks if the tile an ant stepped on was white or black
                    if direction == "T":
                        direction = "R"
                    elif direction == "R":
                        direction = "B"
                    elif direction == "B":
                        direction = "L"
                    elif direction == "L":
                        direction = "T" 
                elif grid[grid_y][grid_x] == "*":
                    grid[grid_y][grid_x] = "."
                    if direction == "T":
                        direction = "L"
                    elif direction == "R":
                        direction = "T"
                    elif direction == "B":
                        direction = "R"
                    elif direction == "L":
                        direction = "B" # Changes direction of ant based on colour of tile
                self.x = x
                self.y = y
                self.direction = direction # Sets object properties into variables


ant1 = Ant(info1[0], info1[1], info1[2])
ant2 = Ant(info2[0], info2[1], info2[2]) # Creates 2 objects that uses the class ant

# Shows the grid that the ants will be traversing on in a visual form (this can be done with a for loop, but I prefer to look at it like this)
grid = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
]

while True:
    moves = int(input("\nInput the amount of moves you want to pass. ")) # Prompts user for input
    if moves == -1:
        exit() # Terminates program as requested
    for i in range(moves):
        ant1.move(int(ant1.x), int(ant1.y), str(ant1.direction))
        ant2.move(int(ant2.x), int(ant2.y), str(ant2.direction)) # Calls back to the class and makes it move the ant
    print("") # Formatting text
    for i in range(11):
        for j in range(11):
            print(grid[i][j], end=" ") # Prints the updated grid
        print("")
    if ant1.x == 99:
        print("Removed")
    else:
        print(int(ant1.x), int(ant1.y), str(ant1.direction))
    if ant2.x == 99: # Checks if either ant is at the borders where I sent it, and if so, shows that it has left the simulation
        print("Removed")
    else:
        print(int(ant2.x), int(ant2.y), str(ant2.direction))
