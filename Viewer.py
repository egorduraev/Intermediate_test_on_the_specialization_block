import Model

def createNote():
    name = input('Введите заголовок заметки: ')
    description = input('Введите тело заметки: ')
    return Model.Note(name = name, description = description)

def menu():
    print("\nКоманды:\nshow - вывести все заметки;\nadd - добавить заметку;\ndelete - удалить заметку;\nedit - редактировать заметку;\nfind - найти заметку по дате;\nid - вывести заметку по id;\nexit - выход из программы.\n\nВведите команду: ")

def add():
    note = createNote()
    array = Model.readFile()
    for notes in array:
        if Model.Note.getId(note) == Model.Note.getId(notes):
            Model.Note.setId(note)
    array.append(note)
    Model.writeFile(array, 'a')
    print('Заметка успешно сохранена')

def show(text):
    flag = True
    array = Model.readFile()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            flag = False
            print(Model.Note.output(notes))
        if text == 'id':
            flag = False
            print('ID: ' + Model.Note.getId(notes))
        if text == 'date':
            flag = False
            if date in Model.Note.getDate(notes):
                print(Model.Note.output(notes))
    if flag == True:
        print('Нет заметок')


def edit(text):
    id = input('Введите id заметки: ')
    array = Model.readFile()
    flag = True
    for notes in array:
        if id == Model.Note.getId(notes):
            flag = False
            if text == 'edit':
                note = createNote()
                Model.Note.setName(notes, note.getName())
                Model.Note.setDescription(notes, note.getDescription())
                Model.Note.setDate(notes)
                print('Заметка отредактирована')
            if text == 'delete':
                array.remove(notes)
                print('Заметка удалена')
            if text == 'show':
                print(Model.Note.output(notes))
    if flag == True:
        print('Заметка не найдена')
    Model.writeFile(array, 'a')