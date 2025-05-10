#!/usr/bin/env python3

def word_frequencies(filename):
    word_count = {}
    target_words = ['Project', 'Gutenberg', 'EBook', 'of']
    with open(filename, "r") as f:
        text = f.read()
    splitting=text.split()
    words=[word.strip("""!"#$%&'()*,-./:;?@[]_""") for word in splitting]
    for word in words:
            if word in target_words:
                if word in word_count:
                  word_count[word] += 1
                else:
                    word_count[word] = 1
            # L.append(f"{r}\t{g}\t{b}\t{name}")
    for word in target_words:
        count = word_count.get(word, 0)
        print(f"{word} {count}")


def main():
    filename = r"C:\Users\kim28\source\repos\Python\SorenPy\PythonData-1\øvelser\e24_word_frequencies\src\alice.txt"
    word_frequencies(filename)

if __name__ == "__main__":
    main()
