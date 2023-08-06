def pig_latin(text):
    data = text.split()
    transformed_words = []

    for word in data:
        final_word = word[1:] + word[0] + "ay"
        transformed_words.append(final_word)

    return " ".join(transformed_words)

print(pig_latin("hello how are you"))  # Output: "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Output: "rogrammingpay niay ythonpay siay unfay"