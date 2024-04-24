import uuid
from datetime import datetime

class Note:
    def __init__(self, id = str(uuid.uuid1())[0:3], name = "Название", description = "Описание", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.name = name
        self.description = description
        self.date = date

    def getId(note):
        return note.id
    
    def getName(note):
        return note.name

    def getDescription(note):
        return note.description

    def getDate(note):
        return note.date
    
    def setId(note):
        note.id = str(uuid.uuid1())[0:3]

    def setName(note, name):
        note.name = name

    def setDescription(note, description):
        note.description = description

    def setDate(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def toString(note):
        return note.id + ';' + note.name + ';' + note.description + ';' + note.date

    def output(note):
        return '\nId: ' + note.id + '\n' + 'Название: ' + note.name + '\n' + 'Описание: ' + note.description + '\n' + 'Дата: ' + note.date

def writeFile(array, mode):
    file = open("notes.csv", mode = 'w', encoding = 'utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode = mode, encoding = 'utf-8')
    for notes in array:
        file.write(Note.toString(notes))
        file.write('\n')
    file.close


def readFile():
    try:
        array = []
        file = open("notes.csv", "r", encoding = 'utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            element = n.split(';')
            note = Note(
                id = element[0], name = element[1], description = element[2], date = element[3])
            array.append(note)
    except Exception:
        print('Заметки отсутствуют')
    finally:
        return array