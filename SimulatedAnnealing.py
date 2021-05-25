from Graph import Graph
from Solution import Solution
import numpy as np
from OptimizationUtils import OptimizationUtils

class SimulatedAnnealing:
    '''
    class which contains heuristic
    '''
    def __init__(self, graph: Graph, solution: Solution):
        self.graph = graph
        self.solution = solution
    def _create_neighbour(self, target: int):
        '''
        method for creating neighbouring solution to a given solution
        by swaping two oligonucleotides with the smallest overlap
        :param solution: Solution object, input solution
        :param target: index of an overlap / first element of a pair to be swapped
        :return: Solution object, input solution with two least overlapping vertices swapped
        '''
        # swap
        (self.solution.id_list[target], self.solution.id_list[target + 1]) = (self.solution.id_list[target + 1], self.solution.id_list[target])
        # assign vertex indices !!! to left_id and right_id
        # left and right refers to the position AFTER the swap
        left_id = self.solution.id_list[target]
        right_id = self.solution.id_list[target + 1]
        # recalculate neighbouring overlaps
        # if the swapped pair was not the first one in the sequence
        if target > 0:
            o = self.graph.compute_overlap(left_id - 1, left_id, 'out')
            self.solution.overlaps[target - 1] = o
        # vertices from the original pair, always in the sequence
        o = self.graph.compute_overlap(left_id, right_id, 'out')
        self.solution.overlaps[target] = o
        # if the swapped pair was not the last one in the sequence
        if target + 1 < len(self.solution.id_list) - 1:
            o = self.graph.compute_overlap(right_id, right_id + 1, 'out')
            self.solution.overlaps[target + 1] = o
    def solve_sa(self):
        self._create_neighbour(10)