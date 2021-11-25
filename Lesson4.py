documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def search_owner(number):
    for elem in documents:
        if elem['number'] == number:
            return print(elem['name'])
    return print('Документ не найден в базе')


def search_directories(number):
    for keys in directories.keys():
        for value in directories.get(keys):
            if value == number:
                return print('Документ хранится на полке: {0}'.format(keys))

    return print('Документ не найден в базе')


def full_info():
    for elem in documents:
        for keys in directories:
            for value in directories.get(keys):
                if elem['number'] == value:
                    print('№: {0}, тип: {1}, владелец: {2}, полка хранения: {3} '.format(elem['number'], elem['type'],
                                                                                         elem['name'], keys))

def new_directories(number):
    if list(directories.keys()).count(number):
        print('Такая полка уже существует. Текущий перечень полок: {0}'.format(list(directories.keys())))
    else:
        directories.update({number: []})
        print('Полка добавлена. Текущий перечень полок: {0}'.format(list(directories.keys())))


def delete_directories(number):
    if list(directories.keys()).count(number):
        if not directories[number]:
            del directories[number]
            print('Полка удалена, текущий список полок: {0}'.format(list(directories.keys())))
        else:
            print('На полке {0} есть документы!, удалите их перед удалением полки'.format(number))
    else:
        print('Такой полки не существует. Текущий перечень полок: {0}'.format(list(directories.keys())))







param = ''
while param != 'q':
    param = input('Введите команду: ')
    if param == 'p':
        number = input('Введите номер документа: ')
        search_owner(number)
    if param == 's':
        number = input('Введите номер документа: ')
        search_directories(number)
    if param == 'l':
        full_info()
    if param == 'ads':
        number = input('Введите номер полки: ')
        new_directories(number)
    if param == 'ds':
        number = input('Введите номер полки: ')
        delete_directories(number)