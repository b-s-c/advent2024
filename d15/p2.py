inDirections = False
grid = []
directions = ""

def expand(line):
    return line.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')

for line in open('real.input'):
    if len(line.strip()) == 0:
        inDirections = True
        continue
    if not inDirections:
        grid.append(list(expand(line.strip())))
        continue
    directions += line.strip()

def mod_10(n):
    return n % 10
def print_garden(g):
    print(' '.ljust(2), " ".join(list(map(str, map(mod_10, range(0, len(g[0])))))))
    for i, line in enumerate(g):
        print(str(i).ljust(2), " ".join(line))

def move(grid, s, v, hor):
    moved = False
    if grid[s[0] + v[0]][s[1] + v[1]] == '.':
        moved = True
        grid[s[0] + v[0]][s[1] + v[1]] = '@'
    elif grid[s[0] + v[0]][s[1] + v[1]] == '#':
        pass
    elif grid[s[0] + v[0]][s[1] + v[1]] in ('[', ']'):
        search = [(s[0] + v[0], s[1] + v[1])]
        canMove = False
        if hor:
            check = (s[0] + v[0], s[1] + v[1])
            while True:
                check = (check[0] + v[0], check[1] + v[1])
                if grid[check[0]][check[1]] == '[':
                    search.append(check)
                elif grid[check[0]][check[1]] == ']':
                    search.append(check)
                elif grid[check[0]][check[1]] == '.':
                    canMove = True
                    break
                elif grid[check[0]][check[1]] == '#':
                    break
        else:
            to_check = [s for s in search]
            search_vals = [grid[s[0] + v[0]][s[1] + v[1]]]
            while to_check:
                check = to_check.pop(0)
                if grid[check[0]][check[1]] == '[':
                    if check not in search:
                        search.append(check)
                        search_vals.append('[')
                    if (check[0], check[1] + 1) not in search:
                        to_check.append((check[0], check[1] + 1))
                    if (check[0] + v[0], check[1] + v[1]) not in search:
                        to_check.append((check[0] + v[0], check[1] + v[1]))
                elif grid[check[0]][check[1]] == ']':
                    if check not in search:
                        search.append(check)
                        search_vals.append(']')
                    if (check[0], check[1] - 1) not in search:
                        to_check.append((check[0], check[1] - 1))
                    if (check[0] + v[0], check[1] + v[1]) not in search:
                        to_check.append((check[0] + v[0], check[1] + v[1]))
                elif grid[check[0]][check[1]] == '.':
                    canMove = True
                elif grid[check[0]][check[1]] == '#':
                    canMove = False
                    break
                print(f'check: {check}')
                print(f'to check: {to_check}')
                print(f'search: {search}')
                print(f'search_vals: {search_vals}')
                print()

        print(f'found {search}')
        print(f'can move? {canMove}')
        moved = canMove

        if canMove:
            if hor:
                for coord in reversed(search):
                    grid[coord[0] + v[0]][coord[1] + v[1]] = grid[coord[0]][coord[1]]
            else:
                for i in range(len(search) - 1, -1, -1):
                    coord = search[i]
                    value = search_vals[i]
                    grid[coord[0]][coord[1]] = '.'
                    grid[coord[0] + v[0]][coord[1] + v[1]] = value


    if moved:
        grid[s[0]][s[1]] = '.'
        grid[s[0] + v[0]][s[1] + v[1]] = '@'
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
        pos = move(grid, pos, v, False)
    if dir == 'v':
        v = (1, 0)
        pos = move(grid, pos, v, False)
    if dir == '<':
        v = (0, -1)
        pos = move(grid, pos, v, True)
    if dir == '>':
        v = (0, 1)
        pos = move(grid, pos, v, True)
    print(dir)
    print_garden(grid)
    print()
    #exit()

p1_total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '[':
            p1_total += 100 * i + j
print(p1_total)
