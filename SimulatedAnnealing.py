from Graph import Graph
from Solution import Solution
import copy
import numpy as np

class SimulatedAnnealing:
    '''
    class which contains heuristic
    '''
    def __init__(self, graph: Graph, solution: Solution, steps: int, init_temp: int):
        self.graph = graph
        self.solution = solution
        self.steps = steps
        self.init_temp = init_temp
        # abbreviate
        from OptimizationUtils import OptimizationUtils
        self.obj = OptimizationUtils.get_objective_value
    def _create_neighbour(self, target: int):
        '''
        method for creating neighbouring solution to a given solution
        by swaping two oligonucleotides with the smallest overlap
        :param target: int, target overlap/vertex pair to swap
        :return: Solution object, input solution with two least overlapping vertices swapped
        '''
        # copy solution
        solution = copy.deepcopy(self.solution)
        # swap
        (solution.id_list[target], solution.id_list[target + 1]) = (solution.id_list[target + 1], solution.id_list[target])
        # assign vertex indices !!! to left_id and right_id
        # left and right refers to the position AFTER the swap
        left_id = solution.id_list[target]
        right_id = solution.id_list[target + 1]
        # recalculate neighbouring overlaps
        # if the swapped pair was not the first one in the sequence
        if target > 0:
            o = self.graph.compute_overlap(solution.id_list[target - 1], left_id, 'out')
            solution.overlaps[target - 1] = o
        # vertices from the original pair, always in the sequence
        o = self.graph.compute_overlap(left_id, right_id, 'out')
        solution.overlaps[target] = o
        # if the swapped pair was not the last one in the sequence
        if target + 1 < len(solution.id_list) - 1:
            o = self.graph.compute_overlap(right_id, solution.id_list[target + 2], 'out')
            solution.overlaps[target + 1] = o
        return solution
    def _get_rand_swap_target(self):
        '''
        method for choosing a new target for _create_neighbour method
        :return: int, target
        '''
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
        considered_overlaps = np.squeeze(np.asarray(considered_overlaps))
        # for numpy shape requirements
        if considered_overlaps.shape == tuple():
            considered_overlaps = np.asarray([considered_overlaps])
        overlap_id = np.random.choice(considered_overlaps)
        return overlap_id
    def _P(self, delta_E: int, temp:int):
        '''
        the probability acceptance function.
        if unif(0, 1) is < P then accept worse new solution
        :param delta_E: int, E(s_new) - E(s)
        :param temp: int, current temp = 10 / step
        :return: float, normalized value for comparison with unif(0, 1)
        '''
        if delta_E < 0:
            return 1.
        else:
            return np.exp(-1 * delta_E / temp) + .01
    def solve_sa(self):
        '''
        simulated annealing algorithm
        :return: Solution, solution vector
        '''
        print(self.solution)
        for step in range(self.steps):
            target = self._get_rand_swap_target()
            s_new = self._create_neighbour(target)
            delta_E = self.obj(s_new) - self.obj(self.solution)
            temp = 10. / (step + 1)
            P = self._P(delta_E, temp)
            #if np.random.uniform(0, 1) < P:
            print(target)
            if delta_E < 0:
                print(self.obj(s_new))
                print(self.obj(self.solution))
                print(delta_E)
                print('###')
                self.solution = s_new