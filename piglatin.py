input = input("Enter the English\n")
def isvowel(ch):
    if "aeiouy".count(ch) >= 1:
        return True
    else:
        return False
count = 0
array = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
if input.count(' ') > 0:
    input = input.split()
    a = -1
    b = len(input)
    while a < b - 1:
        a = a + 1
        z = input[a]
        if z[0] in array:
            e = z + 'a'
            input[a] = e
            pass
        else:
            vowelIndex = [isvowel(ch) for ch in z].index(True)
            zb = z[:vowelIndex]
            d = z[(vowelIndex)::]
            e = d + zb + "a"
            input[a] = e
    input = str(input)
    input = input.replace("'","")
    input = input.replace(",","")
    input = input.replace("[","")
    input = input.replace("]","")
    print(input)
else:
    if input[0] in array:
        print(input + 'a')
    else:
        vowelIndex = [isvowel(ch) for ch in input].index(True)
        zb = input[:vowelIndex]
        d = input[(vowelIndex)::]
        e = d + zb + "a"
        print(e)
