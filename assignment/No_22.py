#removing duplicate from a List

sample = input("Enter numbers in list: ")
sample1 = sample.split()
print("The input is : ",sample1)
output =[]
for i in sample1:
    if i not in output:
        output.append(i)

print("The output is : ",output)
