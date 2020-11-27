#adding 'ing' to the string if it already has adding 'ly'

sample = input("Enter the string: ")
output = ''
if len(sample)<3:
    print(sample)
elif(sample[-3::] == 'ing'):
    print(sample+'ly')
else:
    print(sample+'ing')
