import string


def strip_punctuations(line):
    for character in string.punctuation:
        line = line.replace(character, "")
    return line


filepath = "../szavakGyakorisagaPython/EgriCsillagok.txt"
zCount = 0
word_count = {}

with open(filepath, 'r', encoding='utf-8') as fi:
    for line in fi:
        line = strip_punctuations(line)
        words = line.split()

        for word in words:
            word = word.lower()

            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

list(word_count.keys())[:10]

ten_words = list(word_count.keys())[:0]
for word in ten_words:
    print("{0:15}{1:8d}".format(word, word_count[word]))


def order_dict_by_freq(dictionary):
    sorted_values = []
    for key in dictionary:
        sorted_values.append((dictionary[key], key))
    sorted_values = sorted(sorted_values)
    sorted_values = sorted_values[::-1]
    return sorted_values


top_words = order_dict_by_freq(word_count)[:20]
for tuple_freq in top_words:
    count, word = tuple_freq
    print("{0:15}{1:8d}".format(word, count))

if word.charAt(0)=="z":
    zCount +=1
