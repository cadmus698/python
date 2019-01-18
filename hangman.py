def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]
word = input("Enter the word.\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
a = len(word)
z = 8
b = []
while a > 0:
    a = a-1
    b.append("_")
d = str(b)
d = d.replace("'","")
d = d.replace(",","")
d = d.replace("[","")
d = d.replace("]","")
print(d)
while True:
    guess = input("\nGuess the letter.\n")
    if "give" in guess or "GIVE" in guess or "Give" in guess:
        print("Ok.")
        print("The word was", word)
        break
    elif guess in word:
        e = findOccurrences(word, (guess))
        zdxc = len(e)
        if zdxc > 1:
            el = (len(e)) + 1
            while el >= 0:
                el = el - 1
                dx = e[el - 1]
                b[dx] = (guess)
            print("Good job!")
            d = str(b)
            d = d.replace("'","")
            d = d.replace(",","")
            d = d.replace("[","")
            d = d.replace("]","")
            print("\n",d)
            x = d
            x = x.replace("'","")
            x = x.replace(",","")
            x = x.replace("[","")
            x = x.replace("]","")
            x = x.replace(" ","")
            
        else:
            zds = word.find(guess)
            b[zds] = (guess)
            print("Good job!")
            d = str(b)
            d = d.replace("'","")
            d = d.replace(",","")
            d = d.replace("[","")
            d = d.replace("]","")
            print("\n",d)
            x = d
            x = x.replace("'","")
            x = x.replace(",","")
            x = x.replace("[","")
            x = x.replace("]","")
            x = x.replace(" ","")
    elif guess not in word:
        if z == 0:
            print("You lost! Sorry!")
            print("The word was", word)
            break
        else:
            z = str(int(z)-1)
            print("Nope!")
            zaxcv = ("You have " + z + " mistakes left.")
            if int(z) == 0:
                print("You lost! Sorry!")
                print("The word was '" + word + "'")
                break
            
            else:
                print(zaxcv)
                print("Good luck!")
                x = d
                x = x.replace("'","")
                x = x.replace(",","")
                x = x.replace("[","")
                x = x.replace("]","")
                x = x.replace(" ","")
    if x.count("_") == 0:
        break
    
    if z == 0:
        print("You lost! Sorry!")
        print("The word was", word)
        break