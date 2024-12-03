import re
import math

program = "".join([program.strip() for program in open('real.input')])

mults_p1 = []
mults_p2 = []

def find_mults(s) -> list[str]:
    return re.findall(r'mul\(\d+,\d+\)', s)

mults_p1 = find_mults(program)

while ("don't" in program):
    dont_i = program.rfind("don't()")
    do_i = program.rfind("do()")
    if do_i > dont_i:
        mults_p2.extend(find_mults(program[do_i:]))
    program = program[:max(do_i, dont_i)]
mults_p2.extend(find_mults(program))

print(sum([math.prod(map(int, re.findall(r'\d+', mult))) for mult in mults_p1]))
print(sum([math.prod(map(int, re.findall(r'\d+', mult))) for mult in mults_p2]))
