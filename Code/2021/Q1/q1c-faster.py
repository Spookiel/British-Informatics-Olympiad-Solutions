# see https://reasoning.page/30391/bio-2021-question-1 for an explanation of how this works

from functools import lru_cache

@lru_cache
def arrangements(nodes: int) -> int:
    if nodes == 1:
        return 1
    total = 0
    for i in range(1, nodes):
        total += arrangements(i) * arrangements(nodes - i)
    return total

print(arrangements(24))
