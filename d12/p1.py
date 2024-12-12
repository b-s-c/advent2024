garden = [list(line.strip()) for line in open('real.input')]

def print_garden(garden):
    print(' '.ljust(2), " ".join(list(map(str, range(0, len(garden))))))
    for i, line in enumerate(garden):
        print(str(i).ljust(2), " ".join(line))

print_garden(garden)

def get_starting_point(garden, checked):
    for i in range(0, len(garden)):
        for j in range(0, len(garden)):
            if (i, j) not in checked:
                return ((i, j), garden[i][j])
    return False

def flood_fill(garden, start_coords, symbol):
    result = set()
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
            for n in neighbours:
                if n[0] < 0 or n[0] >= len(garden) or n[1] < 0 or n[1] >= len(garden[n[0]]):
                    perimeter += 1
                    continue
                if garden[n[0]][n[1]] != symbol:
                    perimeter += 1
                to_check.append(n)
    return result, perimeter

checked = set()

p1_total = 0

while len(checked) < len(garden)*len(garden[0]):
    (start_i, start_j), symbol = get_starting_point(garden, checked)
    #print("starting at", (start_i, start_j), "with symbol", symbol)
    this_coords, perimeter = flood_fill(garden, (start_i, start_j), symbol)
    checked = checked.union(this_coords)
    #print(this_coords, perimeter)
    #print("checked", checked)
    print("result", len(this_coords), "*", perimeter, "=", len(this_coords) * perimeter)
    p1_total+=len(this_coords)*perimeter
    
print(p1_total)
