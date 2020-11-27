#if a given string starts with a given character

sample_strings = ["hello","world","love","life","watermelon","apple"]
print("given strings: ",sample_strings)
sample_char = input("Enter a character: ")
result = list(filter(lambda x: x[0]==sample_char,sample_strings))
print(f"{result} starts with {sample_char}")
