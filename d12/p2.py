garden_og = [list(line.strip()) for line in open('real.input')]

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

def find_consecutive_strings(lst):
    total = 0
    in_string = False
    for i in range (0, len(lst) - 1):
        if lst[i] + 1 == lst[i+1]:
            in_string = True
            continue
        else:
            if in_string:
                total += 1
            in_string = False
    if in_string:
        total += 1
    return total



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


    print("edges:", edges)

    edges_vertical = {}
    for k in edges.keys():
        lst = edges[k]
        for item in lst:
            if item in edges_vertical:
                edges_vertical[item].append(k)
            else:
                edges_vertical[item] = [k]

    print("edges vertical:", edges_vertical)

    total_edge_count = 0
    for k in edges.keys():
        edges[k] = sorted(edges[k]) #unnecessary but whatever
        vals = edges[k]
        current_edge = set()
        valid = True
        edge_count = find_consecutive_strings(vals)


        total_edge_count += edge_count

    for k in edges_vertical.keys():
        edges_vertical[k] = sorted(edges_vertical[k]) #unnecessary but whatever
        vals = edges_vertical[k]
        edge_count = 0
        current_edge = set()
        valid = True
        edge_count = find_consecutive_strings(vals)


        total_edge_count += edge_count

    print("total edges:", total_edge_count)

    return result, total_edge_count

checked = set()

p2_total = 0

while len(checked) < len(garden_3x)*len(garden_3x[0]):
    (start_i, start_j), symbol = get_starting_point(garden_3x, checked)
    #print("starting at", (start_i, start_j), "with symbol", symbol)
    this_coords, edges = flood_fill(garden_3x, (start_i, start_j), symbol)
    checked = checked.union(this_coords)
    print(this_coords)
    #print("checked", checked)
    print(symbol, "result", len(this_coords) // 9, "*", edges, "=", (len(this_coords)//9) * edges)
    p2_total+=((len(this_coords) // 9)*edges)

print(p2_total)
