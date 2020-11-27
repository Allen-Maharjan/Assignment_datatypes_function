#smallest number from a list

sample = input("Enter the numbers: ")
output = sample.split()
smallest = int(output[0])
for i in output:
    if(smallest > int(i)):
        smallest = int(i)

print('The smallest number is: ',smallest)
