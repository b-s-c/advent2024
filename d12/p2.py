garden_og = [list(line.strip()) for line in open('test2.input')]

garden_3x = []
for row in garden_og:
    garden_3x_row = []
    for item in row:
        garden_3x_row.extend([item, item, item])
    garden_3x.append(tuple(garden_3x_row))
    garden_3x.append(tuple(garden_3x_row))
    garden_3x.append(tuple(garden_3x_row))
    garden_3x_row.clear()

def mod_10(n):
    return n % 10
def print_garden(g):
    print(' '.ljust(2), " ".join(list(map(str, map(mod_10, range(0, len(g)))))))
    for i, line in enumerate(g):
        print(str(i).ljust(2), " ".join(line))

print_garden(garden_og)
print()
print_garden(garden_3x)

def get_starting_point(garden, checked):
    for i in range(0, len(garden)):
        for j in range(0, len(garden)):
            if (i, j) not in checked:
                return ((i, j), garden[i][j])
    return False

def flood_fill(garden, start_coords, symbol):
    result = set()
    all_neighbours = set()
    edges = dict()
    perimeter = 0
    to_check = [start_coords]
    while to_check:
        #print(to_check)
        coords = to_check.pop(0)
        if coords in result:
            continue
        if garden[coords[0]][coords[1]] == symbol:
            result.add(coords)
            neighbours = (
                            (coords[0] + 1, coords[1]),
                            (coords[0] - 1, coords[1]),
                            (coords[0], coords[1] + 1),
                            (coords[0], coords[1] - 1)
                            )
            is_edge = False
            for n in neighbours:
                all_neighbours.add(n)
                if n[0] < 0 or n[0] >= len(garden) or n[1] < 0 or n[1] >= len(garden[n[0]]):
                    is_edge = True
                    perimeter += 1
                    continue
                if garden[n[0]][n[1]] != symbol:
                    is_edge = True
                    perimeter += 1
                to_check.append(n)
            if is_edge:
                if coords[0] in edges:
                    edges[coords[0]].append(coords[1])
                else:
                    edges[coords[0]] = [coords[1]]
    
    print("edges", edges, len(edges))
    print("neighbours", neighbours)

    return result, perimeter

checked = set()

p1_total = 0

while len(checked) < len(garden_3x)*len(garden_3x[0]):
    (start_i, start_j), symbol = get_starting_point(garden_3x, checked)
    #print("starting at", (start_i, start_j), "with symbol", symbol)
    this_coords, perimeter = flood_fill(garden_3x, (start_i, start_j), symbol)
    checked = checked.union(this_coords)
    print(this_coords)
    #print("checked", checked)
    print(symbol, "result", len(this_coords), "*", perimeter, "=", len(this_coords) * perimeter)
    p1_total+=len(this_coords)*perimeter
    
print(p1_total)
