tmap = [list(map(int, list(line.strip()))) for line in open('real.input')]

def print_grid():
    for i, row in enumerate(tmap):
        print(str(i).rjust(2), row)
    print()

def find_all_zeros(tmap):
    zeros = set()
    for i, row in enumerate(tmap):
        for j, item in enumerate(row):
            if item == 0:
                zeros.add((i, j))
    return zeros

def get_neighbours(tmap, coords, search_value):
    i, j = coords
    neighbour_locations = (
        (i - 1, j    ),
        (i + 1, j    ),
        (i    , j - 1),
        (i    , j + 1),
        )
    results = []
    for loc in neighbour_locations:
        ni, nj = loc
        if ni < 0 or ni >= len(tmap) or nj < 0 or nj >= len(tmap[i]):
            continue
        if tmap[ni][nj] == search_value:
            results.append((ni, nj))
    return results

print_grid()
zero_coords = find_all_zeros(tmap)
print(zero_coords)

p1_total = 0
p2_total = 0

for zc in zero_coords:
    nines_reached = set()
    routes_to_check = [(0, zc)]
    for r in routes_to_check:
        value = r[0] + 1
        coords = r[1]
        valid_neighbours_coords = get_neighbours(tmap, coords, value)
        for vnc in valid_neighbours_coords:
            if value == 9:
                p2_total += 1
                nines_reached.add(vnc)
                continue
            routes_to_check.append((value, vnc))
    p1_total += len(nines_reached)

print(p1_total)
print(p2_total)
