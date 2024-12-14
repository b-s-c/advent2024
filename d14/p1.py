robots = []
with open('real.input') as inp:
    inp = inp.readlines()
    for line in inp:
        p, v = line.strip().split(' ')
        px, py = p.split('=')[1].split(',')
        vx, vy = v.split('=')[1].split(',')
        robots.append(((int(py), int(px)), (int(vy), int(vx)))) # swapping x and y to plug in to 2d array

for r in robots:
    print(r)

h = 7
w = 11
h = 103
w = 101
#t = 100


for t in range(1000, 100000000):
    if t % 1000 == 0:
        print(f'progress: t={t}')
    space = [[0] * w for _ in range(h)]
    valid = True
    for robot in robots:
        px, py = robot[0]
        vx, vy = robot[1]
        mx = (px + t*vx) % h
        my = (py + t*vy) % w
        space[mx][my] += 1
        if space[mx][my] > 1:
            valid = False
            break

    if not valid:
        continue
    else:
        print(f't = {t}')
        for s in space:
            print("".join(map(str, s)))
        input("tree?")
        continue

    quadrant_sums = [0,0,0,0]
    for i, row in enumerate(space):
        for j, val in enumerate(space[i]):
            if val == 0:
                continue
            if i < len(space)//2:
                if j < len(space[i])//2:
                    quadrant_sums[0] += val
                elif j > len(space[i])//2:
                    quadrant_sums[1] += val
            elif i > len(space)//2:
                if j < len(space[i])//2:
                    quadrant_sums[2] += val
                elif j > len(space[i])//2:
                    quadrant_sums[3] += val
    if quadrant_sums[0] == quadrant_sums[1] and quadrant_sums[2] == quadrant_sums[3]:
        print(f't = {t}')
        for s in space:
            print("".join(map(str, s)))
        input("tree?")

for s in space:
    print("".join(map(str, s)))

from math import prod
print(prod(quadrant_sums))
