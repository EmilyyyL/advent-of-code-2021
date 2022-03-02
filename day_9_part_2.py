from sys import stdin

def get_basin(i, j, height_map):
    size = 0
    if i >= 0 and i < len(height_map) and j >= 0 and j < len(height_map[i]):
        if height_map[i][j] != -1 and height_map[i][j] < 9:
            height_map[i][j] = -1
            size = 1
            size += get_basin(i - 1, j, height_map) 
            size += get_basin(i, j - 1, height_map)
            size += get_basin(i + 1, j, height_map)
            size += get_basin(i, j + 1, height_map)
    return size


height_map = []
for line in stdin:
    height_map.append(list(map(int, line.strip())))

basins = []
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
            basins.append(get_basin(i, j, height_map))

basins.sort(reverse=True)
print(f"Multiplying the 3 largest basins together: {basins[0] * basins[1] * basins[2]}")
