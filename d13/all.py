claw_machines = []
with open('real.input') as inp:
    while True:
        a_line = inp.readline().strip()
        if not a_line:
            break
        b_line = inp.readline().strip()
        prize_line = inp.readline().strip()
        blank = inp.readline()
        #print(a_line.split('+'), b_line, prize_line.split('='))
        x1 = a_line.split('+')[1].split(',')[0]
        y1 = a_line.split('+')[-1]
        x2 = b_line.split('+')[1].split(',')[0]
        y2 = b_line.split('+')[-1]
        xs = prize_line.split('=')[1].split(',')[0]
        ys = prize_line.split('=')[-1]
        
        claw_machines.append(tuple(map(int, (x1, x2, y1, y2, int(xs)+10000000000000, int(ys)+10000000000000))))


def calculate(x1, x2, y1, y2, xs, ys):
    a = (xs - (x2/y2)*(ys))/(x1-y1*(x2/y2))
    b = (ys - (y1)*a) / y2
    a = round(a)
    b = round(b)
    if (xs != a*x1 + b*x2) or (ys != a*y1 + b*y2):
        return (-1,-1)
    return (a, b)

total = 0

for cm in claw_machines:
    print("claw", cm)
    a, b = calculate(*cm)
    if a == -1:
        continue
    print(a, b, 3*a + b)
    total += (3*a + b)
    
print(total)
