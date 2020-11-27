#lambda function

sample = int(input("Enter a number to be added: "))
sample1 = int(input("Enter the value of x to be multiplied: "))
sample2 = int(input("Enter the value of y to be multiplied: "))
addi = lambda x : x + 15
mul = lambda x,y : x * y

print(f"When {sample} is added 15 we get",addi(sample))
print(f"When {sample1} and {sample2} are multiplied we get",mul(sample1,sample2))
