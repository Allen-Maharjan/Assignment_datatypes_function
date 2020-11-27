#removing a key from dictionary

sample_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(f"initail_dict = {sample_dict}")
key = int(input("Enter the key to be removed: "))
sample_dict.pop(key)
print(sample_dict)
