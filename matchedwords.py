def match_words(words):
    chr = 0
    lst = []
    for i in words:
        if i[0] == i[-1]:
            lst.append(i)
            chr += 1
    return chr

letters = ["abba", "baba", "aaa", "ccca", "dfed", "hiih"]
count = match_words(letters)

print("the number of matching words is:", count)

