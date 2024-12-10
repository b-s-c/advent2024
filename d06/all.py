def get_grid():
    grid = [list(line.strip()) for line in open('real.input')]
    return grid

grid = get_grid()

directions = ['^', '>', 'v', '<']

def print_grid():
    for i, l in enumerate(grid):
        print(i, l)
    print()

start=()
for i, row in enumerate(grid):
    for j, col in enumerate(row):
       if '^' in col:
           start = (i, j)

print_grid()
print("start", start)

visited = set()

def move(start):
    #print_grid()

    if grid[start[0]][start[1]] == '^':
        dir = 0
        to_check = (start[0] - 1, start[1])
    if grid[start[0]][start[1]] == '>':
        dir = 1
        to_check = (start[0], start[1] + 1)
    if grid[start[0]][start[1]] == 'v':
        dir = 2
        to_check = (start[0] + 1, start[1])
    if grid[start[0]][start[1]] == '<':
        dir = 3
        to_check = (start[0], start[1] - 1)


    if to_check[0] not in range(len(grid)) or to_check[1] not in range(len(grid)):
        return (-1, -1)

    obj = grid[to_check[0]][to_check[1]]

    grid[start[0]][start[1]] = 'X'
    visited.add(start)

    if obj == '#':
        dir = (dir + 1) % 4
        dir_sym = directions[dir]
        grid[start[0]][start[1]] = dir_sym
        return start
    else:
        dir_sym = directions[dir]
        grid[to_check[0]][to_check[1]] = dir_sym
        return to_check
        

while (start[0] in range(len(grid)) and start[1] in range(len(grid[0]))):
    start = move(start)
    if start == (-1, -1):
        break

#print(visited)
print(len(visited) + 1)

max_steps = len(visited) + 1

invalid_count = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        visited = set()
        grid = get_grid()
        valid_start = True
        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if '^' in col:
                    start = (x, y)
                    grid[x][y] = '^'
                    if i == x and j == y:
                        valid_start = False
        if not valid_start:
            continue
        grid[i][j] = '#'
        valid = True
        step_counter = 0
        while (start[0] in range(len(grid)) and start[1] in range(len(grid[0]))):
            start = move(start)
            if start == (-1, -1):
                break
            step_counter += 1
            if step_counter > len(grid) * len(grid) + 1:
                invalid_count += 1
                print("invalids:", invalid_count)
                break


print(invalid_count)
