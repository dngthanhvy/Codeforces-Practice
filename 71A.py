# If the length of the word is strictly more than 10, abbreviate the word so that the word is composed of only the first
# and the last letter, and between them the number of letters between the first and the last.

n = int(input())
words = []

for i in range(0, n):
    words.append(str(input()))


def abbr_words(list_words):
    for elem in list_words:
        if len(elem) > 10:
            print(elem[:1] + str(len(elem[1:-1])) + elem[-1])
        else:
            print(elem)


abbr_words(words)