#sum all item in the list

sample = input("Enter the numbers to be added: ")
output = sample.split()
print("list= ",output)
sample = 0
for i in output:
    sample += int(i)
print("The sum is: ",sample)
