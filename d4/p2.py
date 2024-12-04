grid = [(line.strip()) for line in open('real.input')]

combos = [
    ('M', 'S',
     'M', 'S'),
    ('S', 'M',
     'S', 'M'),
    ('S', 'S',
     'M', 'M'),
    ('M', 'M',
     'S', 'S')
]

count = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        val = grid[i][j]
        if val != "A":
            continue            
        combo = (grid[i - 1][j - 1], grid[i - 1][j + 1], grid[i + 1][j - 1], grid[i + 1][j + 1])
        if combo in combos:
            count += 1
            
print(count)
