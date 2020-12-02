#checking whether the string is number or not

sample_strings = input("Enter a string: ")
result = list(filter(lambda x : x.isdigit(), sample_strings))
print(f"In {sample_strings} {result} is digit")
