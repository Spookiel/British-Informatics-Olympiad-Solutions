

"""
Solution coming soon
"""
from copy import deepcopy


def solve(actors):

    print(actors)
    ways = 0
    scenes = sum(actors)

    startState = ([[] for i in range(len(actors))], set())

    looking = [startState]

    while looking:
        nextState, total = looking.pop(0)
        #print(nextState, total)


        possible = set(range(1, sum(actors)+1))-total

        for actorInd,actor in enumerate(nextState):
            if not actor:
                for scene in possible:
                    copState = deepcopy(nextState)
                    copTotal = deepcopy(total)
                    copState[actorInd].append(scene)
                    copTotal.add(scene)
                    looking.append((copState,copTotal))
            else:
                for scene in possible:
                    if len(actor) < actors[actorInd]:
                        for scene in possible:
                            if scene > actor[-1]:
                                copState = deepcopy(nextState)
                                copTotal = deepcopy(total)
                                copState[actorInd].append(scene)
                                copTotal.add(scene)
                                looking.append((copState, copTotal))






solve([3,2])


def solve(curScene, )