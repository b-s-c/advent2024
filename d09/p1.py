diskmap = open('test.input').readline().strip()

print(diskmap)

free_space = []

final_disk = []

for i, digit in enumerate(diskmap):
    #print("i: {}, digit: {}".format(i, digit))
    #print("final: {}".format(final_disk))
    #print("free: {}".format(free_space))

    if i % 2 == 0:
        values = [i // 2] * int(digit)
    else:
        values = [None] * int(digit)
        free_space.extend(list(range(len(final_disk), len(final_disk) + int(digit))))

    #print("values: {}".format(values))

    final_disk.extend(values)
    #print()

def get_rightmost_valid_index(disk):
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] == None:
            continue
        else:
            #disk = disk[:i+1]
            return i

print()

while free_space:
    #print("final: {}".format(final_disk))
    #print("free: {}".format(free_space))
    i = get_rightmost_valid_index(final_disk)
    if i < free_space[0]:
        break
    val = final_disk.pop(i)
    final_disk[free_space.pop(0)] = val


print(final_disk)
print(free_space)
print(sum([final_disk[i] * i for i in range(0, len(final_disk)) if final_disk[i] != None]))
