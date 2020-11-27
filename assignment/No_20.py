#counting the number of strings with same first and last characters

sample = input("Enter list of words: ")
sample_list = sample.split()
print('list= ',sample_list)
count = 0
for i in range(len(sample_list)):
    if len(sample_list[i]) >= 2:
        if(sample_list[i][0] == sample_list[i][-1]):
            count += 1

print('count= ',count)
