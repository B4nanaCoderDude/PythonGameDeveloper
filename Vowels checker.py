def vowelcheck(text):
    characters={}
    for ch in "aeiou":
        characters[ch]=0
    for ch in text.lower():
        if ch in characters:
            characters[ch]+=1
    for value in characters.values():
        if value==0:
            return False
    return True
answer=input("Choose a sentence to check.")
pop=vowelcheck(answer)
if pop==True:
    print("Your sentence contains all vowels")
if pop==False:
    print("Your sentence does not contain all vowels.")