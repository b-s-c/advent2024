l1 = []
l2 = []
total_distance = 0

with open('real.input') as input:
    for line in input:
        line = line.strip().split()
        l1.append(int(line[0]))
        l2.append(int(line[1]))
    
l1.sort()
l2.sort()

for i in range(len(l1)):
    total_distance += abs(l1[i] - l2[i])
    
print(total_distance)
