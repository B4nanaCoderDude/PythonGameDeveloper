def digitchecker(answer):
    digits={}
    for ch in "1234567890":
        digits[ch]=0
    for ch in answer:
        if ch in digits:
            digits[ch]+=1
    for value in digits.values():
        if value==0:
            return False
    return True
number=input("Type a random number")
checkvalue=digitchecker(number)
if checkvalue==True:
    print("Your number contains all digits.")
if checkvalue==False:
    print("Your number does not contain all digits.")