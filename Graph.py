from Vertex import Vertex
class Graph:
    '''
    Graph handler class
    '''
    def __init__(self):
        self.oligonucleotides_vertices_list = list()
    def add_vertices_list(self, vertices: list):
        for i in range(len(vertices)):
            vertex = Vertex()
            vertex.value = vertices[i]
            vertex.id = i
            self.oligonucleotides_vertices_list.append(vertex)