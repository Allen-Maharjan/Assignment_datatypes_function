#generating string from first 2 and last 2 strings

Input = input("Enter string: ")
if len(Input) < 2:
    print("Empty string")
else:
    print(Input[0:2]+Input[-2::])
