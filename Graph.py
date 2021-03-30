from Vertex import Vertex
from tqdm import tqdm
from time import sleep

class Graph:
    '''
    Graph handler class.
    Vertices are oligonucleotides
    Arcs are metric values computed between two vertices
    metric(a, b) = { (length of nucleotides - overlap) if overlap is not equal to 0
                   { -1 if there is no overlap
    '''
    def __init__(self):
        self.oligonucleotides_list = list()
        self.vertices_no = int()
        self.vertex_value_length = int()
        self._graph_matrix = list()
    def _check_graph_matrix_empty(self):
        '''
        method for reassuring if graph matrix is already created
        :raises: ValueError if graph matrix is not yet created
        '''
        if not self._graph_matrix:
            raise ValueError('graph matrix not created')
    def __str__(self):
        self._check_graph_matrix_empty()
        print('\nGRAPH MATRIX DISPLAY')
        for row in range(self.vertices_no):
            for col in range(self.vertices_no):
                print(self._graph_matrix[row][col], end='\t')
            print('')
        return str()
    def __repr__(self):
        return self.__str__()
    def add_vertices_list(self, vertices: list):
        '''
        method for generating list of Vertex objects.
        gives Vertex.value and Vertex.id and
        sets self.vertices_no param and self.vertex_value_length param
        :param vertices: list of String values of nulceotieds (from .txt file)
        '''
        for i in range(len(vertices)):
            vertex = Vertex()
            vertex.value = vertices[i]
            vertex.id = i
            self.oligonucleotides_list.append(vertex)
        self.vertex_value_length = len(self.oligonucleotides_list[0].value)
        self.vertices_no = len(self.oligonucleotides_list)
    def _compute_metric(self, a: Vertex, b: Vertex):
        # TODO: debug this method - cannot reverse first string
        '''
        method for computing metric used for weighting graph's arcs
        :param a: frist vertex
        :param b: second vertex
        :return: computed metric value
        '''
        first = a.value[::-1]
        second = b.value
        # iterator i is also an overlap value
        i = 0
        while True:
            if first[i] == second[i]:
                i += 1
                # TODO: problem degradation for no errors assumption.
                # repetition treated as no match at all
                # remove below if statement after implementing this part of problem
                if i == self.vertex_value_length:
                    return -1
            else:
                break

        # returns -1 if no match at all
        if i == 0:
            return -1
        else:
            return self.vertex_value_length - i
    def create_graph_matrix(self):
        '''
        method for creating graph matrix.
        It is a (self.vertices_no x self.vertices_no) matrix in which
        vertices are Vertex objects which store nucleotides values
        and arcs are weights equal to computed metric
        '''
        if not self.oligonucleotides_list:
            raise ValueError('empty list of nucleotides')
        for row in range(self.vertices_no):
            self._graph_matrix.append(list())
        print('creating graph matrix...')
        for row in tqdm(range(self.vertices_no)):
            for col in range(self.vertices_no):
                self._graph_matrix[row].append(self._compute_metric(self.oligonucleotides_list[row], self.oligonucleotides_list[col]))
                if row == col:
                    self._graph_matrix[row][col] = -1
        sleep(1)
        print('graph creation finished with success')
    def get_graph_matrix_element(self, i: int, j: int):
        '''
        getter method for graph matrix elements
        :param i: row
        :param j: column
        :return: graph_matrix[i][j] value
        '''
        self._check_graph_matrix_empty()
        return self._graph_matrix[i][j]
    def set_graph_matrix_element(self, i: int, j: int, value: int):
        '''
        setter method for graph matrix elements
        :param i: row
        :param j: column
        :param value: value for graph_matrix[i][j] to be set
        '''
        self._graph_matrix[i][j] = value
    def get_vertex_neighbours(self, i: int) -> list:
        '''
        method for getting most optimal connection from current vertex to the next vertex
        :param i: current vertex id
        :return: id of highest arc value which comes out of current vertex
        '''
        self._check_graph_matrix_empty()
        return self._graph_matrix[i]
