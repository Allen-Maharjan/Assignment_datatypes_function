#program to get single strings from two strings and swap first two

sample1 = input("Enter the first string: ")
sample2 = input("Enter the second string: ")
first,second = sample1[0:2], sample2[0:2]
print(second+sample1[2::], first+sample2[2::])
