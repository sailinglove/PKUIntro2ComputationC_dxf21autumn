N = input()

lst = list(map(int,input().split()))

s = set()

s.update(lst)

print(len(s))

s = sorted(s)
for i in s:
    print(i, end=' ')
print()