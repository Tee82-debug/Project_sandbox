houses = [
    [115910, 4, 128],
    [48718, 3, 210],
    [28977, 2, 58],
    [36932, 3, 79],
    [83903, 3, 111]
]


for h in houses:
    h.append(h[0]/ h[2])
for h in houses:
    print(h)

print(price)
Total_sum = sum(price)
print(Total_sum)

h1 = houses[0][0] / houses[0][2]
print(h1)