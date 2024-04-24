import Viewer

def begin():
    enter = ''
    while input != 'exit':
        Viewer.menu()
        enter = input().strip()
        if enter == 'show':
            Viewer.show('all')
        if enter == 'add':
            Viewer.add()
        if enter == 'delete':
            Viewer.show('all')
            Viewer.edit('delete')
        if enter == 'edit':
            Viewer.show('all')
            Viewer.edit('edit')
        if enter == 'find':
            Viewer.show('date')
        if enter == 'id':
            Viewer.show('id')
            Viewer.edit('show')
        if enter == 'exit':
            break
