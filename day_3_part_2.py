from sys import stdin

bits = []
for line in stdin:
    bits.append(line.strip())

max_num = bits.copy()
min_num = bits.copy()

while len(max_num) > 1:
    for i in range(len(max_num[0])):
        result_max = {}
        for j in range(len(max_num)):
            result_max[max_num[j][i]] = result_max.get(max_num[j][i],0) + 1
        result_max = sorted(result_max.items(), reverse=True)
        max_num = [x for x in max_num if x[i] == max(result_max, key=lambda item:item[1])[0]]   

while len(min_num) > 1:
    for i in range(len(min_num[0])):
        result_min = {}
        for j in range(len(min_num)):
            result_min[min_num[j][i]] = result_min.get(min_num[j][i],0) + 1
        result_min = sorted(result_min.items())
        min_num = [x for x in min_num if x[i] == min(result_min, key=lambda item:item[1])[0]]
        
oxygen_generator_rating = int("".join(max_num), 2)
co2_scrubber_rating = int("".join(min_num), 2)

print(oxygen_generator_rating, co2_scrubber_rating)
print(f"Life Support Rating: {oxygen_generator_rating * co2_scrubber_rating}")