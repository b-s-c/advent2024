import itertools

grid = [list(line.strip()) for line in open('real.input')]

def print_grid():
    for i, row in enumerate(grid):
        print(str(i).rjust(2), row)
    print()

def square(n):
    return abs(n * n)

def get_antinodes(p1, p2):
    diff = (p1[0] - p2[0], p1[1] - p2[1])
    ans = []
    #an1 = (p1[0] + diff[0], p1[1] + diff[1])
    #an2 = (p1[0] - 2*diff[0], p1[1] - 2*diff[1])
    for i in range(-len(grid), len(grid) + 1):
        ans.append((p1[0] + i*diff[0], p1[1] + i*diff[1]))
    return ans


print_grid()

frequencies = {}

for i, row in enumerate(grid):
    for j, frequency in enumerate(row):
        if frequency == '.':
            continue
        if frequency in frequencies:
            frequencies[frequency].append((i, j))
        else:
            frequencies[frequency] = [(i, j)]

print(frequencies)
print()

an_count = 0
seen_ans = set()
total_ans = 0

for f in frequencies.keys():
    combos = itertools.combinations(frequencies[f], 2)
    for combo in combos:
        antinodes = get_antinodes(combo[0], combo[1])
        print(f, combo, antinodes)
        for an in antinodes:
            if (an[0] >= 0 and an[0] < len(grid) and an[1] >= 0 and an[1] < len(grid)):
                if grid[an[0]][an[1]] == '.':
                    grid[an[0]][an[1]] = '#'
                seen_ans.add(an)
                total_ans += 1
    print()

print_grid()
print(len(seen_ans))
print(total_ans)
