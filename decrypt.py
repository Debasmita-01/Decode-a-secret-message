# define a power (function) that finds the truth by shifting the letter by the specified amount
def lassoLetter( letter, shiftAmount ):
    # use the ord power to translate the letter to a special number called its ASCII code 
    # and associate it codename letterCode
    letterCode = ord(letter.lower())
    
    # shift the ASCII code to find the true letter's ASCII code
    # (my team says that ASCII codes are in order, starting with the code for the letter a)
    trueLetterCode = ord("a") + ((letterCode - ord("a"))+shiftAmount) % 26
   
    # now reveal the true letter by using the chr power to translate back from ASCII
    # "return" this as a result of invoking the power lassoLetter
    return chr(trueLetterCode)

    # define a power (function) that finds the truth
# by shifting all the letters in a word by the specified amount
def lassoWord( word, shiftAmount ):
    # this codename (variable) will be updated to store the true phrase after shifting
    trueWord = ""
    
    # for each letter in the word
    for letter in word:
        # invoke the power (function) lassoLetter to reveal the true letter
        # and update the codename trueWord
        trueWord = trueWord + lassoLetter( letter, shiftAmount )

    # return the truth
    return trueWord

# try out the power on the phrase
print( "Shifting terra by 13 gives: \n" + lassoWord( "terra", 13 ) )


print(lassoWord("WHY",13))
print(lassoWord("oskza",-18))
print(lassoWord("ohupo",-1))
print(lassoWord("ED",25))
