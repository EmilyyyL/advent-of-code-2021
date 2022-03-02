# Not a very optimised solution

thingy = list(map(int, input().split(",")))
fuel = []

for i in range(len(thingy)):
    tmp = 0
    for t in thingy:
        th = abs(t - i)
        while th > 0:
            tmp += th
            th -= 1
    fuel.append(tmp)

print(f"Fuel spent: {min(fuel)}")