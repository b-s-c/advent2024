grid = [(line.strip()) for line in open('real.input')]
grid_t = ["".join(line) for line in zip(*grid, strict=True)]
grid_r = ["".join(reversed(line)) for line in grid]

grid_d1 = []
for i in range(0, len(grid)):
    grid_d1.append((" "*i + grid[i])[:len(grid)])
grid_d1 = ["".join(line) for line in zip(*grid_d1, strict=True)]
temp = []
for i in range(0, len(grid)):
    temp.append(grid[i][:i].rjust(len(grid))) #[i:])
temp = ["".join(line) for line in zip(*temp, strict=True)]
grid_d1.extend(temp)

grid_d2 = []
for i in range(0, len(grid_r)):
    grid_d2.append((" "*i + grid_r[i])[:len(grid_t)])
grid_d2 = ["".join(line) for line in zip(*grid_d2, strict=True)]
temp = []
for i in range(0, len(grid_r)):
    temp.append(grid_r[i][:i].rjust(len(grid_t))) #[i:])
temp = ["".join(line) for line in zip(*temp, strict=True)]
grid_d2.extend(temp)

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
for line in grid_d1:
    count += line.count("XMAS")
    count += line.count("SAMX")
    print(line, count)
print(count)
for line in grid_d2:
    count += line.count("XMAS")
    count += line.count("SAMX")
    print(line, count)
    
print(count)
