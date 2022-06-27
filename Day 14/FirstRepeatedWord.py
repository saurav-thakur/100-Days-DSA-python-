def first_repeated(sentence):
    d = {}
    s = sentence.split(" ")
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1

        else:
            return s[i]

sentence = "Ravi had been saying that he had been there"
print(first_repeated(sentence))