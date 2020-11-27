#multiple all item in the list

sample = input("Enter the numbers to be multiplied: ")
output = sample.split()
print("list= ",output)
sample = 1
for i in output:
    sample *= int(i)
print("The multiple is: ",sample)
