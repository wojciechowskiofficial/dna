from FileIO import FileIO

if __name__ == '__main__':
    fileIO = FileIO()
    lista = list()
    lista.append('test_instances_dir')
    lista.append('random_negative_errors_dir')
    lista.append('9.200-40')
    fileIO.read_file(fileIO.get_absolute_path(lista))