import itertools

equations = []

for line in open('real.input'):
    result, values = line.strip().split(': ')
    values = values.split(' ')
    equations.append((int(result), tuple(map(int, values))))

#print(equations)

def get_combos(l):
    combos = itertools.product('+*|', repeat=l)
    for combo in combos:
        yield combo

#for combo in get_combos(5):
#    print(combo)

num_valid = 0
total_p1 = 0

for eq in equations:
    aim = eq[0]
    num_operations = len(eq[1]) - 1
    combos = get_combos(num_operations)

    #print(aim, eq[1])

    for combo in combos:
        values = list(eq[1])
        total = 0
        for i in range(0, len(combo)):
            #print(combo, i)
            op = combo[i]
            if op == '+':
                values[i+1] = values[i] + values[i+1]
            elif op == '*':
                values[i+1] = values[i] * values[i+1]
            elif op == '|':
                values[i+1] = int(str(values[i]) + str(values[i+1]))
            if total > aim:
                break
        #print(aim, values, combo, values[-1]==aim)
        if values[-1] == aim:
            num_valid += 1
            total_p1 += aim
            break

print(num_valid, total_p1)
