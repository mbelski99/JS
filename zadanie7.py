
def person_print(name, last_name, age, *others): #zmienić kolejność atrybutów w deklaracji
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)

