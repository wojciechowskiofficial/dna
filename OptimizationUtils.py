import numpy as np
from Solution import Solution

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