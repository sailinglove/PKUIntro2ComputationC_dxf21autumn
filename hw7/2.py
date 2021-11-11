T = int(input())

for i in range(T):
    N = int(input())
    pairs = []
    for j in range(N):
        xy = input().split()
        pairs.append([int(x) for x in xy])
    for j in range(N):
        length = len(pairs)
        min = (pairs[0][0] - pairs[1][0])**2 + (pairs[1][0] - pairs[1][1])**2
        for h in range(length-1):
            for k in range(h+1, length):
                temp = (pairs[h][0] - pairs[k][0])**2 + (pairs[h][1] - pairs[k][1])**2
                if temp < min:
                    min = temp
    print(min)
