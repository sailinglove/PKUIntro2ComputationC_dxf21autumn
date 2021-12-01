N, L = map(int, input().split())

d = {}

for i in range(N):
    xy = input()
    if xy in d.keys():
        d[xy] += 1
    else:
        d[xy] = 1

max = 0

for i in d.values():
    if i > max:
        max = i

print(max)