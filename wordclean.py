with open('/Users/mattieuxf/Documents/Python/words_alpha.txt') as wordlist, open('words_cleaned.txt', 'w') as wordlist_cleaned:
    words = wordlist.read()
    words = words.split('\n')
    allowed_characters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_list = [item for item in words if all(char in allowed_characters for char in item)]
    for word in filtered_list:
        wordlist_cleaned.write(word + '\n')
    wordlist_cleaned.close()
    with open('words_cleaned.txt') as i:
        print(i.read())