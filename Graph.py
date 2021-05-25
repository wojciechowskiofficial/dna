from Vertex import Vertex
from tqdm import tqdm
from time import sleep
import numpy as np

class Graph:
    '''
    Graph handler class.
    Vertices are oligonucleotides
    Arcs are metric values computed between two vertices
    metric(a, b) = { (length of nucleotides - overlap) if overlap is not equal to 0
                   { 0 if there is no overlap
    '''
    def __init__(self):
        self.oligonucleotides_list = list()
        self.vertices_no = int()
        self.vertex_value_length = int()
        self._graph_matrix = None

    def _check_graph_matrix_empty(self):
        '''
        method for reassuring if graph matrix is already created
        :raises: ValueError if graph matrix is not yet created
        '''
        if not self._graph_matrix.any() or self._graph_matrix is None:
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
        '''
        method for computing metric used for weighting graph's arcs
        :param a: frist vertex
        :param b: second vertex
        :return: computed metric value
        '''
        # left oligonucleotide
        first = a.value
        # right oligonucleotide
        second = b.value
        # length of oligonucleotides
        l = self.vertex_value_length
        # increasing iterator being the overlap value
        i = 1
        # while there can be an overlap try to find it
        while i < l:
            # cut everything outside of potential overlap
            # then see if reminders are equal (these would be overlaps)
            if first[i:] == second[:l - i]:
                # if yes then return l - (l - i) = i
                break
            i += 1
        # returns i == l if no match at all
        return i
    def create_graph_matrix(self):
        '''
        method for creating graph matrix.
        It is a (self.vertices_no x self.vertices_no) matrix in which
        vertices are Vertex objects which store nucleotides values
        and arcs are weights equal to computed metric
        '''
        if not self.oligonucleotides_list:
            raise ValueError('empty list of nucleotides')
        self._graph_matrix = np.empty(shape=(self.vertices_no, self.vertices_no), dtype=np.intc)
        for row in tqdm(range(self.vertices_no)):
            for col in range(self.vertices_no):
                self._graph_matrix[row][col] = self._compute_metric(self.oligonucleotides_list[row],
                                                                    self.oligonucleotides_list[col])
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
    def get_vertex_neighbours(self, i: int, direction: str) -> list:
        '''
        method for getting vertex in or out neighbours
        :param i: current vertex id
        :param direction: str 'in' or 'out'
        :return: array of arcs (vertex neighbours of specified directioon)
        '''
        self._check_graph_matrix_empty()
        if direction == 'in':
            return self._graph_matrix[:, i]
        elif direction == 'out':
            return self._graph_matrix[i,:]
    def compute_overlap(self, current: int, next: int, direction: str) -> int:
        '''
        method for getting directional overlap between current and next vertex
        :param current: int current vertex
        :param next: int next vertex
        :param direction: str 'in' or 'out' direction
        :return: overlap value i.e. (0, 4, 'in') returns overlap between 4th and 0th
                 oligonucleotide because we look for arc that goes into 0th from 4th
        '''
        if direction == 'in':
            if self.get_graph_matrix_element(next, current) == 0:
                return 0
            else:
                return self.vertex_value_length - self.get_graph_matrix_element(next, current)
        elif direction == 'out':
            if self.get_graph_matrix_element(current, next) == 0:
                return 0
            else:
                return self.vertex_value_length - self.get_graph_matrix_element(current, next)