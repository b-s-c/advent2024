l1 = []
l2 = []
similarity_score = 0
frequency_map = {}

with open('real.input') as input:
    for line in input:
        line = line.strip().split()
        l1.append(int(line[0]))
        l2.append(int(line[1]))
    
for i in range(len(l1)):
    val = l1[i]
    if val not in frequency_map:
        frequency_map[val] = l2.count(val)
    similarity_score += val * frequency_map[val]
    
print(similarity_score)
