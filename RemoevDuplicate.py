data = [1, 3, 5, 6, 3, 5, 6, 1]
res = []

for i in data:
    if i not in res:
        res.append(i)

print(res)
