from functools import lru_cache

stones = list(map(int, open('test2.input').readline().strip().split(' ')))

print(stones)

@lru_cache(maxsize=None)
def evolve(stone):
    if stone == 0:
        return [1]
    stone_str = str(stone)
    stone_len = len(stone_str)
    if stone_len % 2 == 0:
        stone_one = int(stone_str[:stone_len//2])
        stone_two = int(stone_str[stone_len//2:])
        return [stone_one, stone_two]
    return [stone*2024]

map_25x = {}

print(evolve(512072))

for _ in range(6):
    new_stones = []
    for stone in stones:
        new_stones.extend(evolve(stone))

    stones = new_stones
    print(new_stones)
    print(len(new_stones))

exit()
