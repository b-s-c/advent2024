import multiprocessing

# 15000x15000
grid = [(line.strip()) for line in open('real.input')]

#for l in grid:
#    print(l)
#print(len(grid), len(grid[0])); exit()

combos = {
    ('M', 'S',
     'M', 'S'),
    ('S', 'M',
     'S', 'M'),
    ('S', 'S',
     'M', 'M'),
    ('M', 'M',
     'S', 'S')
}

results = []

def chew(start, end):
    count = 0
    for i in range(start, end):
        for j in range(1, len(grid[i]) - 1):
            val = grid[i][j]
            if val != 'A':
                continue
            if (grid[i - 1][j - 1], grid[i - 1][j + 1], grid[i + 1][j - 1], grid[i + 1][j + 1]) in combos:
                count += 1
    print("{0}\t -\t {1} finished with total {2}".format(start, end, count))
    return_dict[start] = count

manager = multiprocessing.Manager()
return_dict = manager.dict()
n_proc = 16
processes = []

target_ranges = list(range(1, len(grid) - 1, len(grid) // n_proc)) + [len(grid) - 1]
for i in range(0, len(target_ranges) - 1):
    start = target_ranges[i]; stop = target_ranges[i + 1]
    processes.append(multiprocessing.Process(target=chew, args=(start, stop)))

for p in processes:
    p.start()
for p in processes:
    p.join()

print("total", sum(return_dict.values()))
