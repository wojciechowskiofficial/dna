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
    l.append('random_positive_errors_dir')
    # l.append('no_errors')
    l.append('58.300+120')
    vertices = fileIO.read_file(fileIO.get_absolute_path(l))
    graph = Graph()
    graph.add_vertices_list(vertices)
    graph.create_graph_matrix()
    greedy = Greedy(graph)
    s = greedy.solve_greedy()
    sa = SimulatedAnnealing(graph, s)
    sa.solve_sa()
