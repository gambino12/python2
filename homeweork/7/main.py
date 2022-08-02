import json
def vvdod():
    global name,comment,number
    name = input('ФИО >> ')
    comment = input('Комментарий >> ')
    number = input('Телефон >> ')

def convert_data():
    vvdod()
    data = (comment,number)
    book ={}
    book[name] = data
    return book

def save_data_json():
    with open('book.json','a',encoding='utf8') as telephon_book:
        telephon_book.writelines(convert_data(),ensure_acscill=False)
        print('')

def load_data_json():
    with open('book.json','r',encoding='utf8') as telephon_book:
        data_from_telephone_book = json.load(telephon_book)
        return data_from_telephone_book
#text = load_data_json()

#print(text)
