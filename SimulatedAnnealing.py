from Graph import Graph
from Solution import Solution
import copy
import numpy as np

class SimulatedAnnealing:
    '''
    class which contains heuristic
    '''
    def __init__(self, graph: Graph, solution: Solution):
        self.graph = graph
        self.solution = solution
        # abbreviate
        from OptimizationUtils import OptimizationUtils
        self.obj = OptimizationUtils.get_objective_value
    def _create_neighbour(self, target: int):
        '''
        method for creating neighbouring solution to a given solution
        by swaping two oligonucleotides with the smallest overlap
        :param solution: Solution object, input solution
        :return: Solution object, input solution with two least overlapping vertices swapped
        '''
        # copy solution
        solution = copy.copy(self.solution)
        # swap
        (solution.id_list[target], solution.id_list[target + 1]) = (solution.id_list[target + 1], solution.id_list[target])
        # assign vertex indices !!! to left_id and right_id
        # left and right refers to the position AFTER the swap
        left_id = solution.id_list[target]
        right_id = solution.id_list[target + 1]
        # recalculate neighbouring overlaps
        # if the swapped pair was not the first one in the sequence
        if target > 0:
            o = self.graph.compute_overlap(left_id - 1, left_id, 'out')
            solution.overlaps[target - 1] = o
        # vertices from the original pair, always in the sequence
        o = self.graph.compute_overlap(left_id, right_id, 'out')
        solution.overlaps[target] = o
        # if the swapped pair was not the last one in the sequence
        if target + 1 < len(solution.id_list) - 1:
            o = self.graph.compute_overlap(right_id, right_id + 1, 'out')
            solution.overlaps[target + 1] = o
        return solution
    def _get_rand_swap_target(self):
        overlaps = np.asarray(self.solution.overlaps)
        # argsort
        argsorted = np.argsort(overlaps)
        overlaps = np.sort(overlaps)
        # create overlap distribution histogram
        uniques = np.unique(overlaps, return_counts=True)
        hist_dict = {uniques[0][i] : uniques[1][i] for i in range(uniques[0].shape[0])}
        # do not consider the optimally connected pairs (with overlaps == l - 1)
        if self.solution.vertex_value_length - 1 in hist_dict.keys():
            overlaps = overlaps[:- hist_dict[self.solution.vertex_value_length - 1]]
            argsorted = argsorted[:- hist_dict[self.solution.vertex_value_length - 1]]
        print(hist_dict)
        gen = iter(hist_dict.keys())
        hist_dict = {key : hist_dict[key] * pow(1 / 2, next(gen)) / self.solution.vertex_value_length for key in hist_dict.keys()}
        print(hist_dict)
        keys = np.asarray(list(hist_dict.keys()))
        values = np.asarray(list(hist_dict.values()))
        values = values / np.linalg.norm(values, ord=1)
        print(np.cumsum(values))

        pass
    def solve_sa(self):
        print(self.solution)
        print(self.obj(self.solution))
        s = self._create_neighbour(np.argmin(self.solution.overlaps))
        print(s)
        print(self.obj(s))
        self._get_rand_swap_target()