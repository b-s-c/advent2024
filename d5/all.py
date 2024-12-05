rules = [(line.strip()) for line in open('real.input')]

before_dict = {}
p1_sum = 0
p2_sum = 0

def insert_to_list(lst, item, rule):
    if len(rule) == 0 or len(lst) == 0:
        lst.append(item)
        return lst
    earliest_slot = len(lst)
    for val in rule:
        if val in lst:
            earliest_slot = min(earliest_slot, lst.index(val))
        else:
            continue

    lst.insert(earliest_slot, item)
    return lst

for rule in rules:
    if '|' in rule:
        before, after = map(int, rule.split('|'))
        print(before, after)
        if before in before_dict:
            before_dict[before].add(after)
        else:
            before_dict[before] = {after}
        if after not in before_dict:
            before_dict[after] = set()
    if ',' in rule:
        update = list(map(int, rule.split(',')))
        valid = True
        seen = set() 
        for i in range(len(update) - 1, 0, -1):
            before = update[i-1]
            after = update[i]
            seen.add(after)
            if seen.issubset(before_dict[before]):
                continue
            else:
                valid = False
                break
        if valid:
            p1_sum += update[(len(update) // 2)]
        else:
            new_update = []
            for item in update:
                print(new_update, item, before_dict[item])
                new_update = insert_to_list(new_update, item, before_dict[item])
                print(new_update, item, before_dict[item])
            print("new", new_update)
            p2_sum += new_update[(len(new_update) // 2)]

print(before_dict)
print(p1_sum)
print(p2_sum)
