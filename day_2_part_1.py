from sys import stdin

depth = 0
horizontal = 0
for line in stdin:
    if "forward" in line:
        horizontal += int(line.split()[1])
    if "down" in line:
        depth += int(line.split()[1])
    if "up" in line:
        depth -= int(line.split()[1])

print(f"Depth x Horizontal = {depth * horizontal}")