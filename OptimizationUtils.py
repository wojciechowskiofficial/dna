import numpy as np
from Solution import Solution
from Graph import Graph

class OptimizationUtils:
    '''
    placeholder for optimization related operations
    '''
    @staticmethod
    def get_objective_value(solution: Solution):
        '''
        method for computing objective function value
        :param solution: Solution object to compute the objective function value over
        :return: int objective function value
        '''
        overlap_vector = np.asarray(solution.overlaps, dtype=np.intc)
        length_vector = np.full(shape=overlap_vector.shape, fill_value=solution.vertex_value_length, dtype=overlap_vector.dtype)
        return np.sum(length_vector - overlap_vector, axis=0)
    @staticmethod
    def get_less_than_n(graph: Graph, solution: Solution, n: int):
        '''
        method for cutting a solution vector <= N from global solution vector.
        estimate window width, iteratively move the window by its width, compute obj. for the window,
        estimate the best subspace of global solution and construct new solution with len(sequence) <= N
        :param graph: Graph, graph from SA
        :param solution: Solution, global solution from SA
        :param n: int, parameter N
        :return: Solution, new adjusted solution object
        '''
        # estimate window width by averaging overlaps
        overlap_vector = np.asarray(solution.overlaps, dtype=np.intc)
        mean = int(np.round(np.mean(overlap_vector)))
        window_width = int(1 + (n - solution.vertex_value_length) / (solution.vertex_value_length - mean))
        # find the best subspace of global solution
        max_value = 0
        max_i = 0
        i = 0
        while i + window_width < overlap_vector.shape[0] - 1:
            window = overlap_vector[i:i + window_width]
            if np.sum(window) > max_value:
                max_i = i
            i += window_width
        # create new solution object
        s = Solution(direction='out', vertex_value_length=solution.vertex_value_length)
        s.add_id(solution.id_list[max_i])
        s.sequence = graph.oligonucleotides_list[max_i].value
        # keep appending until the <= N condition is violated
        while len(s.sequence) <= n:
            overlap = graph.compute_overlap(solution.id_list[max_i], solution.id_list[max_i + 1], 'out')
            max_i += 1
            s.add_id(solution.id_list[max_i])
            s.add_overlap(overlap)
            s.add_sequence(graph.oligonucleotides_list[solution.id_list[max_i]].value, overlap)
        # account for violated condition and reverse last appendix to again satisfy condition
        overflow = s.vertex_value_length - s.overlaps[-1]
        del s.id_list[-1]
        del s.overlaps[-1]
        s.sequence = s.sequence[:-overflow]
        return s