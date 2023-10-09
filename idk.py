N = int(input())

lst = list(map(int, input().split()))

def check(l:lst):
    for i in range(len(lst)):
        sum = 0
        for j in range(i, len(lst)):
            sum += lst[j]
            if sum == N:
                return 'Yes'
            if sum > N:
                break
    return 'No'

print(check(lst))