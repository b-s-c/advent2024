reports = [[int(l) for l in line.strip().split()] for line in open('real.input')]

# 1 asc, 0 desc
def check_pair_direction(val1, val2) -> bool:
    return val1 < val2

# returns (pass/fail, margin of error)
def check_report(report) -> tuple[bool, int]:
    direction_target = check_pair_direction(report[0], report[1])
    for i in range(0, len(report) - 1):
        difference = report[i] - report[i + 1]
        if difference == 0 or difference < -3 or difference > 3 or check_pair_direction(report[i], report[i + 1]) != direction_target:
            return False, i
    return True, 0

total_p1, total_p2 = 0, 0
for report in reports:
    result, error = check_report(report)
    total_p1 += result
    total_p2 += result

    if result == False:
        total_p2 += any(check_report(report[:e] + report[e + 1:])[0] for e in [error, error + 1, error - 1])

print(total_p1, total_p2)
