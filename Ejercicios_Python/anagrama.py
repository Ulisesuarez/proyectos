def anagrams(word, words):
    copyWord=word
    anagramList=[]
    originalWordAsList=list(word)
    for wordList in words:
        
        if len(wordList)==len(word):
            
            for character in wordList:
                
                if word.find(character)!=-1:
                    originalWordAsList[word.find(character)]=""
                   
                word="".join(originalWordAsList)
                originalWordAsList=list(word)
            
            if "".join(originalWordAsList)=="":
                
                    anagramList.append(wordList)
        word=copyWord
        originalWordAsList=list(word)
    return anagramList

print(anagrams("abba",["aabb","bbaa","caab","abac","baab"]))
