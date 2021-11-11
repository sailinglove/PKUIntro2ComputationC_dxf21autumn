N, m = map(int, input().split())

lst = list(map(int, input().split()))

counter = 0

for i in lst:
    if i == m:
        counter += 1

print(counter)