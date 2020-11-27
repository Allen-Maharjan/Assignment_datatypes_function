#insert string in middle

def insert_string_middle(character,sentence):
    num = int(len(character)/2)
    print(num)
    print(character[0:num]+sentence+character[num:len(character)])

character = input("Enter the sign ({},[])= ")
sentence = input("Enter the sentence= ")

insert_string_middle(character,sentence)
