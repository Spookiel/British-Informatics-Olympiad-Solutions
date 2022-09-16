

from collections import defaultdict

class State:
    def __init__(self, triplet):
        self.w, self.d, self.t = triplet

        self.w = int(self.w)
        self.t = int(self.t)
        if self.d == "R":
            self.d = 1
        else:
            self.d = -1


class Tape:
    def __init__(self):
        self.tape = defaultdict(int)
        self.cur_state = 1
        self.tape_pos = 0

    def step(self):

        if self.cur_state == 0:
            return True


        tape_val = self.tape[self.tape_pos]
        nstate = states[(self.cur_state, tape_val)]
        self.tape[self.tape_pos] = nstate.w
        self.tape_pos += nstate.d
        self.cur_state = nstate.t


        return False

    def output(self):

        for p in range(self.tape_pos-3, self.tape_pos+4):
            print(self.tape[p], end="")




states = {}
n = int(input())
for i in range(1,n+1):
    l, r = input().split()
    states[(i, 0)] = State(l)
    states[(i, 1)] = State(r)


tape = Tape()

m = int(input())

for s in range(m):
    done = tape.step()

    if done:
        break
else:
    s += 1
tape.output()
print()
print(s)
