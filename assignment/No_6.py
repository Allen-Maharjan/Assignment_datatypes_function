#replacing not ... poor to good

sample1 = input("Enter a sentence: ")
b = sample1.split()
output = []
a = []
for i in b:
    if i == 'not':
        output.append(b.index('not'))
        output.append(b.index('poor'))

if len(output)<2:
    print("Error")
else:
    del b[output[0]:(output[1]+1)]
    b[output[0]] = 'good,'

print(" ".join(b))
