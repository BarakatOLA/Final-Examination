def unique_consonants_count(input_string):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    unique_consonants = set()

    for letter in string:
       if letter.lower() in consonants:
        if string.lower().count(letter.lower()) == 1:
            unique_consonants.add(letter.lower())

        return len(unique_consonants)

print(unique_consonants_count("cat"))