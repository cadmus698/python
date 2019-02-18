array1 = input('Enter the contents of the first array.\n')
array2 = input('Enter the contents of the second array.\n')
array1 = array1.split(',')
array2 = array2.split(',')
counter = -1
strtoprint = ''
if (len(array1)) > (len(array2)):
    while len(array1) != len(array2):
        array2.append('')
    while counter != len(array1) - 1:
        counter += 1
        strtoprint += (array1[counter] + ',' + array2[counter] + ',')
        
elif (len(array2)) > (len(array1)):
    while len(array2) != len(array1):
        array2.append('')
    while counter != len(array1) - 1:
        counter += 1
        strtoprint += (array1[counter] + ',' + array2[counter] + ',')
        
elif (len(array1)) == (len(array2)):
    while counter != len(array1) - 1:
        counter += 1
        strtoprint += (array1[counter] + ',' + array2[counter] + ',')
strtoprint = strtoprint[:-1]
strtoprint = strtoprint.replace(',,',',')
strtoprint = strtoprint.replace(', ','')
if strtoprint[-1] == ',':
    print(strtoprint[:-1])
else:
    print(strtoprint)