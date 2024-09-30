def single_root_words(root_word, *other_words):
    same_wodrds = []
    root_word_lower = root_word.lower()
    for word in other_words:
        if root_word_lower in word.lower() or word.lower() in root_word_lower:
            same_wodrds.append(word)
    print(same_wodrds)

single_root_words('ANA', 'banan','MELONana','monkey','gg','WATERbananaMELOn')