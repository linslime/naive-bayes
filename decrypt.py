sentence = "Yfqp nx hmjfu\nBmjwj ymjwj nx f xmjqq ymjwj nx f bfd\nXmtb rj ymj htij\n"
sentence = list(sentence)
print("n = 0")
print(''.join(sentence))
print()
for i in range(0, 26):
    for x in range(0,len(sentence)):
        if sentence[x] >= 'a' and sentence[x] <= 'z':
            sentence[x] = chr(ord('z') - (ord('z') - ord(sentence[x]) + 1) % 26)
        if sentence[x] >= 'A' and sentence[x] <= 'Z':
            sentence[x] = chr(ord('Z') - (ord('Z') - ord(sentence[x]) + 1) % 26)
    print("n =", i + 1)
    print(''.join(sentence))
