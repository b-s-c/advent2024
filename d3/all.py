import re
import math

program = "".join([program.strip() for program in open('real.input')])

def calc_mults(s) -> list[str]:
    return sum(math.prod(map(int, tup)) for tup in re.findall(r'mul\((\d+),(\d+)\)', s))

mults_p1 = calc_mults(program)
mults_p2 = 0

while ("don't" in program):
    dont_i = program.rfind("don't()")
    do_i = program.rfind("do()")
    if do_i > dont_i:
        mults_p2 += calc_mults(program[do_i:])
    program = program[:max(do_i, dont_i)]
mults_p2 += calc_mults(program)

print(mults_p1)
print(mults_p2)
