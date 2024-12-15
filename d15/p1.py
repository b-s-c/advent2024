inDirections = False
grid = []
directions = ""
for line in open('real.input'):
    if len(line.strip()) == 0:
        inDirections = True
        continue
    if not inDirections:
        grid.append(list(line.strip()))
        continue
    directions += line.strip()

def print_garden(garden):
    print(' '.ljust(2), " ".join(list(map(str, range(0, len(garden))))))
    for i, line in enumerate(garden):
        print(str(i).ljust(2), " ".join(line))

def move(grid, s, v):
    moved = False
    if grid[s[0] + v[0]][s[1] + v[1]] == '.':
        moved = True
        grid[s[0] + v[0]][s[1] + v[1]] = '@'
    elif grid[s[0] + v[0]][s[1] + v[1]] == '#':
        pass
    elif grid[s[0] + v[0]][s[1] + v[1]] == 'O':
        num_boxes = 1
        coords = [(s[0] + v[0], s[1] + v[1])]
        move = 2
        canMove = True
        while True:
            check_i = s[0] + move*v[0]
            check_j = s[1] + move*v[1]
            check = grid[check_i][check_j]
            coords.append((check_i, check_j))
            if check == 'O':
                num_boxes += 1
            elif check == '.':
                break
            elif check == '#':
                canMove = False
                break
            move += 1
        if canMove:
            moved = True
            while num_boxes > 0:
                coord = coords.pop()
                grid[coord[0]][coord[1]] = 'O'
                num_boxes -= 1
            grid[s[0] + v[0]][s[1] + v[1]] = '@'

    if moved:
        grid[s[0]][s[1]] = '.'
        return (s[0] + v[0], s[1] + v[1])
    else:
        return (s[0], s[1])


pos = (-1,-1)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            pos = (i, j)
            break
    if pos[0] != -1:
        break
print_garden(grid)
print(directions)
print(f'start: {pos}')


for dir in directions:
    if dir == '^':
        v = (-1, 0)
        pos = move(grid, pos, v)
    if dir == 'v':
        v = (1, 0)
        pos = move(grid, pos, v)
    if dir == '<':
        v = (0, -1)
        pos = move(grid, pos, v)
    if dir == '>':
        v = (0, 1)
        pos = move(grid, pos, v)
    print(dir)
    print_garden(grid)
    print()

p1_total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'O':
            p1_total += 100 * i + j
print(p1_total)
