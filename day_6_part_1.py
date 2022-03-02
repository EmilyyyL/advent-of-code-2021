thingy = list(map(int, input().split(",")))
num = int(input())

for i in range(num):
    for t in range(len(thingy)):
        if thingy[t] == 0:
            thingy.append(8)
            thingy[t] = 6
        else:
            thingy[t] -= 1

print(f"FIshies {len(thingy)}")

# Part 1 and part 2 offer the same solution but part 2 is much faster