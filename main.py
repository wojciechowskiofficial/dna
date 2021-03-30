from FileIO import FileIO
from Graph import Graph
from DummyGreedy import DummyGreedy

if __name__ == '__main__':
    fileIO = FileIO()
    lista = list()
    lista.append('test_instances_dir')
    lista.append('custom_instances_dir')
    lista.append('no_errors')
    vertices = fileIO.read_file(fileIO.get_absolute_path(lista))
    graph = Graph()
    graph.add_vertices_list(vertices)
    graph.create_graph_matrix()
    greedy = DummyGreedy(graph)
    greedy.solve()