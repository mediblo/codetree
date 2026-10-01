a = list(map(int, input().split()))
print(abs(sum([a[i] for i in range(10) if i % 2 != 0]) - sum([a[i] for i in range(10) if i % 2 == 0])))