part = set()

for i in range(5000000):
    part.add(str(1000000 + i))

for j in range(5999900, 5999999):
    if str(j) in part:
        print(j)