with open("books/frankenstein.txt", "r") as f:
    file = f.read()


def count_words(input):
    words = input.split()
    return len(words)


def count_characters(input):
    map = dict()
    input = input.replace(" ", "").lower()
    for c in input:
        if c not in map.keys():
            map[c] = 0
        else:
            map[c] += 1
    return map


def report(characters: dict):
    characters = characterssort()
    for (char, count) in characters.items():
        print(f"The '{char}' character was found {count} times")


print(count_words(file))
print(count_characters(file))
print(report(count_characters(file)))
