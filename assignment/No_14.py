#Creating Html tag

def add_tags(tags,words):
    if tags == 'i':
        print('<i>'+words+'</i>')
    elif tags == 'b':
        print('<b>'+words+'</b>')
    elif tags == 'p':
        print('<p>'+words+'</p>')

tags = input("Enter tags= ")
words = input("Enter sentence= ")

add_tags(tags,words)
