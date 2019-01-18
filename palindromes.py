sentence = input("Enter the sentence.\n")
sa = (sentence[::-1])
sa = sa.replace(' ', '')
sentence = sentence.replace(' ', '')




if sa == (sentence):
    print("Your sentence is a palindrome.")
    
elif sentence.lower() == sa.lower():
    print("Your sentence is a palindrome.")
    
else:
    print("Your sentence is not a palindrome.")