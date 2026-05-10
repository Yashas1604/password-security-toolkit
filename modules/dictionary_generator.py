def generate_dictionary(base_words, output_file="wordlist.txt"):
    variations = []
    leet = {'a':'@', 'e':'3', 'i':'1', 'o':'0', 's':'$'}
    
    for word in base_words:
        variations.append(word)
        variations.append(word.capitalize())
        variations.append(word + "123")
        variations.append(word + "!")
        leet_word = ''.join(leet.get(c, c) for c in word.lower())
        variations.append(leet_word)
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(set(variations)))
    
    return {"message": f"Generated {len(variations)} words", "file": output_file}