def single_root_words(root_word,*other_words):
    same_words=[]
    x=0
    end=len(other_words)
    for x in range(end):
        if root_word.lower() in other_words[x].lower() or other_words[x].lower() in root_word.lower():
            same_words.append(other_words[x])
            continue
    return same_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)