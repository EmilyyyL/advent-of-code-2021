from sys import stdin

def add_coord(x, y, result):
    coord = str(x) + "," + str(y)
    result[coord] = result.get(coord,0) + 1


result = {}
for line in stdin:
    start, end = line.strip().split(" -> ")
    start_x, start_y = map(int, start.split(","))
    end_x, end_y = map(int, end.split(","))

    if start_x == end_x:
        while start_y != end_y:
            add_coord(start_x, start_y, result)
            if start_y > end_y:
                start_y -= 1
            else:
                start_y += 1
      
    elif start_y == end_y:
        while start_x != end_x:
            add_coord(start_x, start_y, result)
            if start_x > end_x:
                start_x -= 1
            else:
                start_x += 1
    
    add_coord(start_x, start_y, result)
        
counter = 0
for coord in result:
    if result[coord] >= 2:
        counter += 1

print(f"Dangerous points: {counter}")