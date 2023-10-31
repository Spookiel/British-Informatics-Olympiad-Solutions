#Solution by @Pararcana
print("""Co-ordinates are from 1 - 11")
Directions are T  = Top, B = Bottom, L = Left, R = Right
Please use the format 'x y d' e.g. '1 1 T'\n""") 
position1 = str(input("Input ant 1's co-ordinates and direction: ")).split(" ")
position2 = str(input("Input ant 2's co-ordinates and direction: ")).split(" ")
directions = ["T", "R", "B", "L"]

def rotate(direction, rotation):
  index = directions.index(direction) + rotation
  if index >= 4:
    index -= 4
  return directions[index]
  
class Ant: 
  def __init__(self, x, y, direction): 
    self.x, self.y, self.direction = x, y, direction
    
  def move(self, x, y, direction):
    if not(x <= 0 or x >= 12 or y <= 0 or y >= 12):
      if direction == "R" or direction == "L":
        x += direction == "R" and 1 or -1
      elif direction == "T" or direction == "B":
        y += direction == "T" and 1 or -1
      if x <= 0 or x >= 12 or y <= 0 or y >= 12:
        self.x = 99
      else:
        empty = grid[-y + 11][x - 1] == "."
        grid[-y + 11][x - 1] = empty and "*" or "."
        self.direction = rotate(direction, empty and 1 or -1)
        self.x, self.y = x, y
            
ant1 = Ant(position1[0], position1[1], position1[2])
ant2 = Ant(position2[0], position2[1], position2[2])

grid = []
for _ in range(11):
  grid.append(["."]*11)

while True:
    moves = int(input("\nInput the amount of moves you want to pass. "))
    if moves == -1:
        exit()
    for _ in range(moves):
        ant1.move(int(ant1.x), int(ant1.y), str(ant1.direction))
        ant2.move(int(ant2.x), int(ant2.y), str(ant2.direction))
    print("")
    for i in range(11):
      print(" ".join(grid[i]))
    print(ant1.x == 99 and "Removed" or " ".join([str(ant1.x), str(ant1.y), ant1.direction]))
    print(ant2.x == 99 and "Removed" or " ".join([str(ant2.x), str(ant2.y), ant2.direction]))

    print_grid(grid)
    print(a1)
    print(a2)
