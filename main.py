from FileIO import FileIO
from Graph import Graph
from Greedy import Greedy

if __name__ == '__main__':
    fileIO = FileIO()
    l = list()
    l.append('test_instances_dir')
    l.append('custom_instances_dir')
    # l.append('random_negative_errors_dir')
    l.append('no_errors')
    # l.append('9.200-40')
    vertices = fileIO.read_file(fileIO.get_absolute_path(l))
    graph = Graph()
    graph.add_vertices_list(vertices)
    graph.create_graph_matrix()
    print(graph)
    greedy = Greedy(graph)

    #greedy = DummyGreedy(graph)
    #greedy.solve()
    #print(str(greedy.graph))
    #print(greedy.solution.id_list)
    #print(greedy.solution.sequence)
    #print(greedy.solution.overlaps)
