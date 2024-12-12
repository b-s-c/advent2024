from functools import cache

stones = tuple(map(int, open('big.input').readline().strip().split(' ')))

def evolve(stone):
    if stone == 0:
        return (1,)
    stone_str = str(stone)
    stone_len = len(stone_str)
    if stone_len % 2 == 0:
        stone_one = int(stone_str[:stone_len//2])
        stone_two = int(stone_str[stone_len//2:])
        return (stone_one, stone_two)
    return (stone*2024,)

seen = dict()

@cache
def evolve_recur(stone, n):
    if n <= 1:
        return sum(len(evolve(s)) for s in stone)
    else:
        return sum(evolve_recur(evolve(s), n - 1) for s in stone)

if __name__ == '__main__':
    import time
    start = time.perf_counter()
    print(evolve_recur(stones, 75))
    end = time.perf_counter()
    print(end-start)
