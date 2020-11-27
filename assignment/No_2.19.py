#creating fibonacci series
from functools import reduce
number = int(input("Enter nth number: "))
result=[]
sample_list = [0,1]
for i in range (0, number):
    result = reduce(lambda x,y : x+y,sample_list[i::] )
    sample_list.append(result)
    print(sample_list[i::])
print("Fibonacci sequence:",sample_list)
