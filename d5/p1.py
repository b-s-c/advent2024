rules = [(line.strip()) for line in open('real.input')]

before_dict = {}
p1_sum = 0

for rule in rules:
    if '|' in rule:
        before, after = rule.split('|')
        if before in before_dict:
            before_dict[before].add(after)
        else:
            before_dict[before] = {after}
        if after not in before_dict:
            before_dict[after] = set()
    if ',' in rule:
        update = rule.split(',')
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
        print(update, valid)
        if valid:
            p1_sum += int(update[(len(update) // 2)])
        else:
            pass #p2

print(before_dict)
print(p1_sum)
