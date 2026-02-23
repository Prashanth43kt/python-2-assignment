#input
sentence=input(str("enter the sentence: "))
#original 
print("original:",sentence)
#with the space
print("character(space):",len(sentence))
#without the space
no_space=sentence.replace("","")
print("character(nospace):",len(no_space))
#words
words=sentence.split();
print("word:",len(words))
#upper and lower case
print("upper:",sentence.upper())
print("lower:",sentence.lower())
print("title:",sentence.title())
#first and last words
print("first:",words[0])
print("last:",words[-1])
print("rev:",sentence[::-1])