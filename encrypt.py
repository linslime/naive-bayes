sentence = "Talk is cheap\nWhere there is a shell there is a way\nShow me the code\n"
sentence = list(sentence)
for i in range(0, 26):
    for x in range(0,len(sentence)):
        if sentence[x] >= 'a' and sentence[x] <= 'z':
            sentence[x] = chr(ord('a') + (ord(sentence[x]) - ord('a') + 1) % 26)
        if sentence[x] >= 'A' and sentence[x] <= 'Z':
            sentence[x] = chr(ord('A') + (ord(sentence[x]) - ord('A') + 1) % 26)
    print("n =", i + 1)
    print(''.join(sentence))