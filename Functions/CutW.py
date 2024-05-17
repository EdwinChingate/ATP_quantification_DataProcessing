def CutW(word,left,right): #Get text from a word between 2 defined characteres
    #word: string array to cut
    #left: string left character
    #right: string right character
    iz=word.find(left)
    newword=word[iz+1:]
    der=newword.find(right)
    finalword=newword[:der]
    return finalword
