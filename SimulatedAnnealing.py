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
        # create overlap distribution histogram
        uniques = np.unique(overlaps, return_counts=True)
        hist_dict = {uniques[0][i] : uniques[1][i] for i in range(uniques[0].shape[0])}
        # do not consider the optimally connected pairs (with overlaps == l - 1)
        if self.solution.vertex_value_length - 1 in hist_dict.keys():
            del hist_dict[self.solution.vertex_value_length - 1]
        # create a distribution by multiplying histogram over a geometric decay vector
        gen = iter(hist_dict.keys())
        hist_dict = {key : hist_dict[key] * pow(1 / 4, next(gen)) / self.solution.vertex_value_length for key in hist_dict.keys()}
        # randomize overlap value
        keys = np.asarray(list(hist_dict.keys()))
        values = np.asarray(list(hist_dict.values()))
        normalized_values = values / np.linalg.norm(values, ord=1)
        chosen_overlap = np.random.choice(keys, p=normalized_values)
        # randomize specific pair/specific overlap
        considered_overlaps = np.where(overlaps == chosen_overlap)
        overlap_id = np.random.choice(np.squeeze(np.asarray(considered_overlaps)))
        return overlap_id
    def solve_sa(self):
        print(self.solution)
        print(self.obj(self.solution))
        s = self._create_neighbour(int(np.argmin(self.solution.overlaps)))
        print(s)
        print(self.obj(s))
        print(self._get_rand_swap_target())