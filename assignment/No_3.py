#changing the same characters to $

Input = input("Enter strings: ")
output = ''
for i in Input:
    if (Input[0] == i and output != '' ):
        output += "$"
    else:
        output += i

print(output)
