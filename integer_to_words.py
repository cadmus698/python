def grunt_work(final_output, output, exceptions, a, b):
    if output[a] == 'one' and output[a] not in exceptions:
        final_output.append(output[a] + 'teen')
    
    elif output[a] == 'zero' and output[b] == 'zero':
        pass
    
    elif output[a] == 'zero' and output[b] != 'zero':
        final_output.append(output[b])        
    
    elif output[a] == 'one' and output[b] == 'zero':
        final_output.append('ten')
        
    elif output[a] == 'one' and output[b] == 'one':
        final_output.append('eleven')
    
    elif output[a] == 'one' and output[b] == 'two':
        final_output.append('twelve')
    
    elif output[a] == 'one' and output[b] == 'three':
        final_output.append('thirteen')
        
    elif output[a] == 'one' and output[b] == 'five':
        final_output.append('fifteen')
        
    elif output[a] == 'two' and output[b] != 'zero':
        final_output.append('twenty-' + output[b])
        
    elif output[a] == 'two' and output[b] == 'zero':
        final_output.append('twenty')
        
    elif output[a] == 'three' and output[b] != 'zero':
        final_output.append('thirty-' + output[b])
        
    elif output[a] == 'three' and output[b] == 'zero':
        final_output.append('thirty')
        
    elif output[a] == 'four' and output[b] != 'zero':
        final_output.append('forty-' + output[b])
        
    elif output[a] == 'four' and output[b] == 'zero':
        final_output.append('forty')
        
    elif output[a] == 'five' and output[b] != 'zero':
        final_output.append('fifty-' + output[b])
        
    elif output[a] == 'five' and output[b] == 'zero':
        final_output.append('fifty')
        
    elif output[a] == 'six' and output[b] != 'zero':
        final_output.append('sixty-' + output[b])
        
    elif output[a] == 'six' and output[b] == 'zero':
        final_output.append('sixty')
        
    elif output[a] == 'seven' and output[b] != 'zero':
        final_output.append('seventy-' + output[b])
        
    elif output[a] == 'seven' and output[b] == 'zero':
        final_output.append('seventy')
    
    elif output[a] == 'eight' and output[b] != 'zero':
        final_output.append('eighty-' + output[b])
        
    elif output[a] == 'eight' and output[b] == 'zero':
        final_output.append('eighty')
        
    elif output[a] == 'nine' and output[b] != 'zero':
        final_output.append('ninety-' + output[b])
        
    elif output[a] == 'nine' and output[b] == 'zero':
        final_output.append('ninety')


number = input('Enter the number.\n')
num_length = len(number)
final_output = []
exceptions = ['zero', 'one', 'two', 'three', 'five']
counter = -1
output = []
while counter < (num_length - 1):
    counter += 1
    if number[counter] == '0':
        output.append('zero')
        
    elif number[counter] == '1':
        output.append('one')
         
    elif number[counter] == '2':
        output.append('two')
         
    elif number[counter] == '3':
        output.append('three')
     
    elif number[counter] == '4':
        output.append('four')
        
    elif number[counter] == '5':
        output.append('five')
         
    elif number[counter] == '6':
        output.append('six')
         
    elif number[counter] == '7':
        output.append('seven')
         
    elif number[counter] == '8':
        output.append('eight')
         
    elif number[counter] == '9':
        output.append('nine')
         
output_length = len(output)
if output_length == 1:
    #output = str(output)
    #output.replace('[','')
    #output.replace(']','')
    #output.replace("'","")
    print(output[0])
elif output_length == 2:
    a = 0
    b = 1
    grunt_work(final_output, output, exceptions, a, b)
elif output_length == 3:
    a = 1
    b = 2
    if (output[0] != "zero"):
        final_output.append(output[0] + '-hundred-')
    grunt_work(final_output, output, exceptions, a, b)
elif output_length == 4:
    a = 2
    b = 3
    if (output[0] != "zero"):
        final_output.append(output[0] + '-thousand-')
    if (output[1] != "zero"):
        final_output.append(output[1] + '-hundred-')
    grunt_work(final_output, output, exceptions, a, b)
elif output_length == 5:
    a = 0
    b = 1
    grunt_work(final_output, output, exceptions, a, b)
    final_output[0] = final_output[0] + '-thousand-'
    final_output.append(output[2] + '-hundred-')
    a = 3
    b = 4
    grunt_work(final_output, output, exceptions, a, b)
    
final_output = str(final_output)
final_output = final_output.replace('[','')
final_output = final_output.replace(']','')
final_output = final_output.replace("'","")
final_output = final_output.replace(",","")
final_output = final_output.replace(" ","")
length = (final_output.find('zero'))
if length > 0:
    final_output = (final_output[:(final_output.find('zero'))])
if final_output[-1] == '-':
    final_output = final_output[:-1]
print(final_output)