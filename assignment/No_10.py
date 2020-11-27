#removing odd index

sample = input("Enter a string: ")
for i in range(len(sample)):
    if(i%2 == 0):
        print(sample[i],end='')
