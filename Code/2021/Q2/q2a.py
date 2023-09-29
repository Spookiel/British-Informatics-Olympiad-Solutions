
from typing import List, Tuple

### Coords to Tiles
TRI_LOOK = {}





class Tile:

    def __init__(self, coords):
        assert len(coords)==3
        self.a, self.b, self.c = coords
        self.a, self.b, self.c = coords

        self.val = 0

    @property
    def up(self):
        """Does this triangle point up"""
        return self.a+self.b+self.c==2

    @property
    def coord_tuple(self):
        return self.a, self.b, self.c

    @property
    def edges(self):
        """Returns edges for triangle in clockwise order starting from the left edge"""

        return [(i, self.coord_tuple) for i in range(3)]

    @property
    def adj_tris(self):
        ### Numbering clockwise from the up triangles
        ### 0 is left, 1 is right and 2 is down
        ### 0 is left, 1 is up, 2 is right
        if self.up:
            return [ ### Ensure order of edges matches numbering scheme
                (self.a - 1, self.b, self.c), ### Left edge faces
                (self.a, self.b, self.c - 1),  ### Right edge faces
                (self.a, self.b - 1, self.c), ### Down edge faces

            ]
        else:
            return [
                ### Ensure order of edges matches numbering
                (self.a, self.b, self.c + 1),  ### Right edge faces
                (self.a, self.b + 1, self.c), ## Up edge faces

                (self.a + 1, self.b, self.c),  ### left edge faces
            ]
    def get_facing_triangle(self, edge):
        assert type(edge)==int and 0 <= edge < 3
        return self.adj_tris[edge]


    def get_edges_facing_away(self, tri):
        ### Return all (edge_num, coords) of edges facing away from tri
        #print(self.adj_tris, tri.coord_tuple, "HERE", self.coord_tuple)
        return [k for k in range(3) if self.adj_tris[k]!=tri.coord_tuple]

    def get_scoring_tiles_assuming_corner(self):
        ### Returns 3 possible scoring triangles assuming this tile is the corner of them
        ### Triangles clockwise again

        ### Two cases self is up or down
        ### Left triangle is (self.a-1, self.b, self.c+1), self.coords, (self.a-1, self.b+1, self.c)


        if self.up:

            t1 = [(self.a-1, self.b,self.c+1),(self.a-1, self.b+1, self.c), self.coord_tuple]
            t2 = [self.coord_tuple, (self.a, self.b+1, self.c-1), (self.a+1, self.b, self.c-1)]
            t3 = [(self.a, self.b-1, self.c+1), self.coord_tuple, (self.a+1, self.b-1, self.c)]


        else:
            t1 = [(self.a-1, self.b, self.c+1), self.coord_tuple, (self.a, self.b-1, self.c+1)]
            t2 = [(self.a-1, self.b+1, self.c), (self.a, self.b+1, self.c-1), self.coord_tuple]
            t3 = [self.coord_tuple, (self.a+1, self.b, self.c-1), (self.a+1, self.b-1, self.c)]
        #print(t1, t2, t3)
        return t1, t2,t3


    def check_if_scores(self, playernum):
        ### If the other two tiles are filled with value then player wins if played here

        to_check = self.get_scoring_tiles_assuming_corner()


        for tile_list in to_check:

            to_check = [i for i in tile_list if i!=self.coord_tuple]
            scores = True
            for tri_coord in to_check:
                #print(tri_coord, "HERE")
                if tri_coord not in TRI_LOOK:
                    TRI_LOOK[tri_coord] = Tile(tri_coord)

                tri_obj = TRI_LOOK[tri_coord]

                if tri_obj.val!=playernum:
                    scores = False
            if scores:
                return True
        return False


class Perim:
    def __init__(self, ftriang: Tile):

        ### Flat edges are zero and then Clockwise
        self.edges:List[Tuple[int, Tuple[int, int, int]]] = ftriang.edges ### Contains list of edges for player to traverse
        self.tris_in_edges = [] ### Contains coord tuple list of the triangles that are included in the edge list

        self.tris_in_edges.append(ftriang.coord_tuple)

    def add_triangle(self, position, score=0):
        ### Adds new triangle to position in edge list


        ### Two cases: PacMan case, Two edges removed One added
        ### Normal Case: One edge removed two edges added

        ### Case is Pacman if exactly two of the adjacent three triangles are in the edgelist already


        ### You always add the opposite triangle to the perimeter
        ### Eg, If current triangle is a down triangle, then you'll add an up

        cur_edge: int = self.edges[position][0]
        cur_tri_coords = self.edges[position][1]
        cur_tri_obj = TRI_LOOK[cur_tri_coords]

        new_triangle_coords = cur_tri_obj.get_facing_triangle(cur_edge)
        #print("ADDING NEW TRIANGLE", new_triangle_coords, score)
        if new_triangle_coords not in TRI_LOOK:
            TRI_LOOK[new_triangle_coords] = Tile(new_triangle_coords)

        new_tri_obj = TRI_LOOK[new_triangle_coords]


        new_tri_obj.val = score

        #print("REPLACING EDGE", self.edges[position])
        #print(new_tri_obj.get_edges_facing_away(cur_tri_obj))
        if self.count_adj_in_list(new_tri_obj)==2:
            ### Pacman case
            #print("PACMAN CASE")

            ### In PacMan case, the up / down edge is always the free one
            ### Need to remove the next two edges

            if new_tri_obj.up:
                new_edge = (2, new_triangle_coords)
            else:
                new_edge = (0, new_triangle_coords)

            self.edges = self.edges[:position]+[new_edge]+self.edges[position+2:]


        else:
            ### Normal case
            ###Remove edge at the current position
            new_edges = [new_tri_obj.edges[ind] for ind in new_tri_obj.get_edges_facing_away(cur_tri_obj)]


            ### Careful on the order the new edges need to go
            ### If triangle is facing up and the edge being removed is down
            ### Then need to add the new edges in reverse
            ### Or if triangle is facing down and the edge being removed is the right edge
            ### Then edges need to be reversed

            if cur_edge==2 or (not cur_tri_obj.up and cur_edge==0):
                new_edges = new_edges[::-1]

            self.edges = self.edges[:position]+new_edges+self.edges[position+1:]
            ### Add two new edges

        self.tris_in_edges.append(new_tri_obj.coord_tuple)


    def count_adj_in_list(self, triag: Tile):

        c = 0
        for adj in triag.adj_tris:
            if adj in self.tris_in_edges:
                c += 1
        return c


START_COORDS = (0,1,1)
class Player:

    def __init__(self, max_moves, pnum):
        assert type(pnum)==int and 0 < pnum
        self.pnum = pnum
        self.max_moves = max_moves
        self.perim_pos = 0
        self.cedge = None
        self.score = 0


    def reposition(self, perim):

        if self.cedge in perim.edges:
            return


        #print("REPOSITIONING", self.pnum)
        ###Move to top left of the cells

        b = sorted(perim.edges,key=lambda x: (999999-x[1][1], x[1][0])) ### Gets highest leftmost triangle
        #print(b)
        ### Will always have a left edge showing so looking for

        self.perim_pos = perim.edges.index(b[0])
        #print(new_perim_pos)

    def move(self, perim, move_num):

        if self.cedge not in perim.edges:
            self.reposition(perim)
        else:
            self.perim_pos = perim.edges.index(self.cedge)

        self.cedge = perim.edges[self.perim_pos]
        #print(f"PLAYER {self.pnum} STARTING AT {self.perim_pos}, (Edge: {self.cedge}")
        #print(perim.edges)
        spos = int(self.perim_pos)
        for npos in range(self.perim_pos+1, self.perim_pos+self.max_moves+1):

            ### Check if we can score at this position
            npos %= len(perim.edges)
            edge, tri_coords = perim.edges[npos]

            tri_obj = TRI_LOOK[tri_coords]

            if tri_obj.check_if_scores(self.pnum):
                #if move_num!=m:
                self.score += 1
                break
        self.perim_pos = int(npos)
        self.cedge = perim.edges[self.perim_pos]



        perim.add_triangle(spos, self.pnum)

        #print(f"PLAYER {self.pnum} ENDING AT {self.perim_pos}, (Edge: {self.cedge}")



### (0,1,1) is one of the two up facing triangles
TRI_LOOK[START_COORDS] = Tile(START_COORDS)
perim = Perim(TRI_LOOK[START_COORDS])

"""
perim.add_triangle(1)
perim.add_triangle(1)
perim.add_triangle(3)

TRI_LOOK[(0,1,1)].val = 1
TRI_LOOK[(0,2,0)].val = 1

print(TRI_LOOK[(1,1,0)].check_if_scores(1))"""


p, m = list(map(int, input().split()))
mlen = list(map(int, input().split()))

players = [Player(mlen[i], i+1) for i in range(p)]

for p in range(len(players)):
    players[p].cedge = perim.edges[players[p].perim_pos]

cp = 0
for mnum in range(m):
    players[cp].move(perim, mnum)
    for p2 in players:
        p2.reposition(perim)
    cp += 1
    cp %= len(players)

    """
    for player in players:
        print(f"AT END OF TURN PLAYER {player.pnum} IS AT EDGE {player.perim_pos} and EDGE VAL {player.cedge}")
    """
for i in range(len(players)):
    print(players[i].score)

print(len(perim.edges))


