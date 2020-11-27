#checking whether a key exist or not

sample_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(f"sample dictionary = {sample_dict}")
key = int(input("Enter the key to check: "))
if key in sample_dict:
    print('key found')
else:
    print("key not found")
