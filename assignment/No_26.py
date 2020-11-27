#insert given string at begining of all item

sample = input('Enter the list: ')
sample_list = sample.split()
string = input("Enter string: ")
output = []
for i in sample_list:
    output.append(string+i)

print(output)
