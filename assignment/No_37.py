#multiply all the values of dictionary

sample_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
output = 1
for i , j in sample_dict.items():
    output *= j

print(output)
