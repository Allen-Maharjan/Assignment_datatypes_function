#printing the longest string

def find_longest(sample):
    s1 = sample.split()
    largest = 0
    for i in s1:
        if (largest<=len(i)):
            largest = len(i)



    return largest


string1 = input("Enter the setence: ")
print("The longest length is: ",find_longest(string1))
