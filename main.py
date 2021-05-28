from FileIO import FileIO
from Graph import Graph
from Greedy import Greedy
from SimulatedAnnealing import SimulatedAnnealing
from OptimizationUtils import OptimizationUtils

if __name__ == '__main__':
    fileIO = FileIO()
    l = list()
    l.append('test_instances_dir')
    #l.append('custom_instances_dir')
    l.append('random_negative_errors_dir')
    # l.append('no_errors')
    l.append('9.200-40')
    vertices = fileIO.read_file(fileIO.get_absolute_path(l))
    graph = Graph()
    graph.add_vertices_list(vertices)
    graph.create_graph_matrix()
    greedy = Greedy(graph)
    s = greedy.solve_greedy()
    n = 209
    sa = SimulatedAnnealing(graph, solution=s, steps=1000, init_temp=10, n=n)
    sa.solve_sa()
    print('K: ', len(sa.solution.id_list), ' N: ', n)