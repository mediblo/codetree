data = list(map(int, input().split()))

total = 0
for i in range(3, len(data)):
    if data[i] == 0:
        total = data[i-1] + data[i-2] + data[i-3]
        break

print(total)