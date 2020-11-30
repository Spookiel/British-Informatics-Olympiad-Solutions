



tiles = [{"green":[1,3], "red":[2,4]}, {"green":[2,4], "red":[1,3]}, {"green":[3,4], "red":[1,2]}, {"green":[1,4], "red":[2,3]}, {"green":[1,2], "red":[3,4]}, {"green":[2,3], "red":[1,4]}]

#1 is west, 2 is north, 3 is east, 4 is south

def canConnect(tile1, tile2, colour):
    directions = []
    for connection1 in tile1[colour]:
        if (connection1-2)%4 in tile2[colour]:
            directions.append(connection1)

    return directions


t0,t1 = tiles[4],tiles[5]

#print(canConnect(t0, t1, "red"))

board = []
tileSet = set()
n = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(n):
        tileSet.add((i,j))

dlook = {1:[0,-1], 2:[-1,0],3:[0,1],4:[1,0]}


rScore, gScore = 0,0
tileSetCopy = set(tileSet)

for col in ["red", "green"]:
    while tileSet:
        nn = tileSet.pop()
        #print(nn, board[nn[1]][nn[0]])
        seen = set()
        queue = [nn]
        while queue:
            nnn = queue.pop(0)
            seen.add(nnn)
            for k,adj in dlook.items():
                nx, ny  = adj[0]+nnn[0], adj[1]+nnn[1]
                try:
                    if canConnect(tiles[board[ny][nx]], tiles[board[nnn[0]][nnn[1]]], col) == k:
                        queue.append(nnn)
                        seen.add(nnn)
                    print("TRYING TO CONNECT", nx, ny, nnn, board[nnn[0]][nnn[1]])
                except Exception as e:
                    pass
                    #print(e, ny, nx, nnn, "HERE")
        print(seen, nn)