from FileIO import FileIO
from Graph import Graph

if __name__ == '__main__':
    fileIO = FileIO()
    lista = list()
    lista.append('test_instances_dir')
    lista.append('random_negative_errors_dir')
    lista.append('9.200-40')
    vertices = fileIO.read_file(fileIO.get_absolute_path(lista))
    graph = Graph()
    graph.add_vertices_list(vertices)