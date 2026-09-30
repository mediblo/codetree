data = list(map(int, input().split()))
print(f"{sum([data[i] for i in range(len(data)) if (i+1) % 2 == 0])} {sum([data[i] for i in range(len(data)) if (i+1) % 3 == 0])/3:.1f}" )