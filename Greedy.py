from Graph import Graph
from Solution import Solution
import numpy as np

class Greedy:
    '''
    Greedy class, which contains subgreedy and greedy algorithm
    '''
    def __init__(self, graph: Graph):
        self.graph = graph
        self.solution = Solution()
    def _queue_candidates(self, v: int, direction: str):
        '''
        method for createing a queue array of candidate vertices to be appended
        :param v: current vertex
        :param direction: desired direction ('in' or 'out')
        :return: array of vertices with descending attractiveness
        '''
        return np.flip(np.argsort(self.graph.get_vertex_neighbours(v, direction)))
    def solve_subgreedy(self, v: int, direction: int):
        '''
        method which applies subgreedy algorithm, saves solution into Solution object
        :param v: starting vertex
        :param direction: desired direction ('in' or 'out')
        '''
        pass
