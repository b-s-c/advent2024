grid = [(line.strip()) for line in open('real.input')]
grid_t = ["".join(line) for line in zip(*grid, strict=True)]
grid_r = ["".join(reversed(line)) for line in grid]

def get_diagonals(grid) -> list[str]:
    temp_1 = [(" "*i + grid[i])[:len(grid)] for i in range(0, len(grid))]
    temp_1 = ["".join(line) for line in zip(*temp_1, strict=True)]
    temp_2 = [grid[i][:i].rjust(len(grid)) for i in range(0, len(grid))]
    temp_2 = ["".join(line) for line in zip(*temp_2, strict=True)]
    temp_1.extend(temp_2)
    return temp_1

print(len(grid), len(grid[0]))

count = 0

for g in (grid, grid_t, get_diagonals(grid), get_diagonals(grid_r)):
    for line in g:
        count += line.count("XMAS")
        count += line.count("SAMX")
        print(line, count)
    
print(count)
