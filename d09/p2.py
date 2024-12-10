diskmap = open('real.input').readline().strip()

print(diskmap)

final_disk = []

for i, digit in enumerate(diskmap):
    #print("i: {}, digit: {}".format(i, digit))
    #print("final: {}".format(final_disk))

    if i % 2 == 0:
        values = (i // 2, int(digit))
    else:
        values = (None, int(digit))

    #print("values: {}".format(values))

    final_disk.append(values)
    #print()

#print("final: {}".format(final_disk))

def find_pair(final_disk, right_start=-1):
    if right_start == -1:
        right_start = len(final_disk)
    for i in range(right_start - 1, -1, -1):
        values = final_disk[i]
        if values[0] != None:
            for j in range(0, i):
                gap = final_disk[j]
                if gap[0] == None:
                    gap_size = gap[1]
                    if gap_size >= values[1]:
                        return i, j
    return -1, -1


#print("\nlast\n")

right_start = len(final_disk)

while True:
    value_i, gap_i = find_pair(final_disk, right_start)
    if gap_i == -1:
        break
    #print(gap_i, final_disk[gap_i], value_i, final_disk[value_i])
    gap_size = final_disk[gap_i][1]
    value_size = final_disk[value_i][1]
    if gap_size - value_size == 0:
        final_disk[gap_i] = final_disk[value_i]
        final_disk[value_i] = (None, value_size)
    else:
        final_disk[gap_i] = final_disk[value_i]
        final_disk[value_i] = (None, value_size)
        final_disk.insert(gap_i + 1, (None, gap_size - value_size))
    right_start = value_i
    #print("final: {}\n".format(final_disk))
    

count = 0
total = 0
for value in final_disk:
    if value[0] == None:
        count += value[1]
        continue
    for i in range(count, count + value[1]):
        total += i * value[0]
    count += value[1]
print(total)
