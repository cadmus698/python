from time import sleep
number = input("Enter the binary\n")
if number == '3.141592':
    print('You have unlocked the secrets of the universe...')
    sleep(1)
    print('Life means 42')
elif '2' in number or '3' in number or '4' in number or '5' in number or '6' in number or '7' in number or '8' in number or '9' in number:
    print('You have entered the matrix...')
    sleep(1)
    print('If you want to meet Morpheus, go to the white rabbit')
    sleep(3)
    while True:
        print('1010011011101000101010111011010101010101010101010101110000110110101001010101001111010101010111100001000101010110101')
        print('1010000111010101011000001010100101010010010101001010111101001010000111110101000010101011010100010010101010101001001')
        print('1101001010011110100101111010011111101001010000101010101011101001001010101001010100101010010111110100000111000110010')
        print('1100101010101010101010011010111100010010010101101001010100110001000100101010101110010101000101010101001011111010101')
        print('1110001010111101010011011111110001010101010100000111100101111010010100101010001010100111000101100101000101001101011')
num_length = (len(number)) - 1
power = num_length
output = 0
while power != -1:
    output += int(number[(num_length - power)]) * (2 ** power)
    power -= 1
print(output)