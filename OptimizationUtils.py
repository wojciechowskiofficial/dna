import numpy as np
from Solution import Solution

class OptimizationUtils:
    @staticmethod
    def get_objective_value(solution: Solution):
        overlap_vector = np.asarray(solution.overlaps, dtype=np.intc)
        length_vector = np.full(shape=overlap_vector.shape, fill_value=solution.vertex_value_length, dtype=overlap_vector.dtype)
        return np.sum(length_vector - overlap_vector, axis=0)