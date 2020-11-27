#largest number from a list

sample = input("Enter the numbers: ")
output = sample.split()
largest = 0
for i in output:
    if(largest < int(i)):
        largest = int(i)

print('The largest number is: ',largest)
