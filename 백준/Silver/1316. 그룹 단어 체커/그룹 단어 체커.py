N = int(input())

for _ in range(N):
    word = input()

    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+2:]:
            N -= 1
            break
print(N)