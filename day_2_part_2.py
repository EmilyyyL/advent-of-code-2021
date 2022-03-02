from sys import stdin

depth = 0
horizontal = 0
aim = 0
for line in stdin:
    value = int(line.split()[1])
    if "forward" in line:
        horizontal += value
        depth += (aim * value)
    elif "down" in line:
        aim += value
    elif "up" in line:
        aim -= value

print(f"Depth x Horizontal = {depth * horizontal}")