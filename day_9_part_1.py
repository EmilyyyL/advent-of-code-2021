from sys import stdin

height_map = []
for line in stdin:
    height_map.append(list(map(int, line.strip())))

risk_level = 0
for i in range(len(height_map)):
    for j in range(len(height_map[i])):
        result = []
        if i - 1 >= 0:
            result.append(bool(height_map[i - 1][j] > height_map[i][j]))
        if i + 1 < len(height_map):
            result.append(bool(height_map[i + 1][j] > height_map[i][j]))
        if j - 1 >= 0:
            result.append(bool(height_map[i][j - 1] > height_map[i][j]))
        if j + 1 < len(height_map[i]):
            result.append(bool(height_map[i][j + 1] > height_map[i][j]))

        if all(result):
            risk_level += (height_map[i][j] + 1)

print(f"Risk Level: {risk_level}")
