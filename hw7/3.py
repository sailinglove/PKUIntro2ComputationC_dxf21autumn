s = input()

searched = ""

no_match = False

for i in range(len(s)):
    if s[i] in searched:
        continue
    else:
        counter = 0
        no_match = True
        for j in range(i+1, len(s)):
            if s[j] == s[i]:
                no_match = False
                break
        if no_match:
            print(s[i])
            break
    searched = searched + s[i]