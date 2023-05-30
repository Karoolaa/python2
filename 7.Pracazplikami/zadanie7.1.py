from os import path

def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        word_count = len(content.split())
        return word_count

dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

words = count_words(data_path)
print(f"Liczba słów: {words}")

def word_stats(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        ending_letters = {}

        for word in words:
            if word[-1] not in ending_letters:
                ending_letters[word[-1]] = 1
            else:
                ending_letters[word[-1]] += 1

        return ending_letters

statistics = word_stats(data_path)
print("Statystyki liter kończących słowa:")
for letter, count in statistics.items():
    print(f"Litera '{letter}': {count}")
