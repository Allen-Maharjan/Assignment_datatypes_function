#sorting alphanumerically

sample = input("Enter the word(with comma): ")
output = sample.split(', ')
output.sort()
output1 = []
for i in output:
    if i not in output1:
        output1.append(i)
print(", ".join(output1))
