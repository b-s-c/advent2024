grid = [(line.strip()) for line in open('real.input')]
grid_t = ["".join(line) for line in zip(*grid, strict=True)]
grid_r = ["".join(reversed(line)) for line in grid]

def get_diagonals(grid) -> list[str]:
    temp_1 = []
    for i in range(0, len(grid)):
        temp_1.append((" "*i + grid[i])[:len(grid)])
    temp_1 = ["".join(line) for line in zip(*temp_1, strict=True)]
    temp_2 = []
    for i in range(0, len(grid)):
        temp_2.append(grid[i][:i].rjust(len(grid))) #[i:])
    temp_2 = ["".join(line) for line in zip(*temp_2, strict=True)]
    temp_1.extend(temp_2)
    return temp_1

print(len(grid), len(grid[0]))

count = 0

for line in grid:
    count += line.count("XMAS")
    count += line.count("SAMX")
    print(line, count)
print(count)
for line in grid_t:
    count += line.count("XMAS")
    count += line.count("SAMX")
    print(line, count)
print(count)
for line in get_diagonals(grid):
    count += line.count("XMAS")
    count += line.count("SAMX")
    print(line, count)
print(count)
for line in get_diagonals(grid_r):
    count += line.count("XMAS")
    count += line.count("SAMX")
    print(line, count)
    
print(count)
