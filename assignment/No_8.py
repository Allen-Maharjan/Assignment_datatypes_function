#removing the nth index character

sample = list(input("Enter a string: "))
remove = int(input ("Enter the index to be removed: "))
del sample[remove]
print(''.join(sample))
