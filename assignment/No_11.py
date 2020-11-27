#Counting the number of characters same as 1

Input = input("Enter strings: ")
output= {}
for i in range(len(Input)):
    count = 0
    if (Input[i]==' '):
        continue
    for j in range(len(Input)):
        if (Input[i] == Input[j]):
            count += 1
    output[Input[i]] = count
print(output)
