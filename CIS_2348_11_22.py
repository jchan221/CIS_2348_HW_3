# Joshua Chan
# 1588459
words = input()
words = words.split()
for i in range(0, len(words)):
    print(words[i], words.count(words[i]))