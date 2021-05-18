from Graph import Graph
from Solution import Solution
import numpy as np

class Greedy:
    '''
    Greedy class, which contains subgreedy and greedy algorithm
    '''
    def __init__(self, graph: Graph):
        self.graph = graph
    def _queue_candidates(self, v: int, direction: str):
        '''
        method for createing a queue array of candidate vertices to be appended
        :param v: current vertex
        :param direction: desired direction ('in' or 'out')
        :return: array of vertices with descending attractiveness
        '''
        return np.flip(np.argsort(self.graph.get_vertex_neighbours(v, direction)))
    def _valid_candidates_left(self, visited: set, queue: np.array) -> bool:
        '''
        method for checking the main subgreedy loop condition
        :param visited: set of visited vertices
        :param queue: np.array of queued neighbours
        :return: bool True if there are valid candidates left else False
        '''
        for i in range(queue.shape[0]):
            if queue[i] not in visited:
                return True
        return False
    def _get_best_candidate(self, visited: set, queue: np.array):
        '''
        method for getting next best candidate inside subgreedy loop
        :param visited: set of visited vertices
        :param queue: np.array of queued neighbours
        :return: id of the next best candidate vertex
        '''
        for i in range(queue.shape[0]):
            if queue[i] not in visited:
                return queue[i]
    def solve_subgreedy(self, v: int, direction: str) -> Solution:
        '''
        method which applies subgreedy algorithm, saves solution into Solution object
        :param v: starting vertex
        :param direction: desired direction ('in' or 'out')
        '''
        # create solution object and init it with v
        solution = Solution(direction)
        solution.id_list.append(v)
        solution.sequence = self.graph.oligonucleotides_list[v].value
        # create necessary variables and data structures
        visited = {v}
        # ensure while loop entrance
        candidates_queue = self._queue_candidates(v, direction)
        is_valid_candidates = self._valid_candidates_left(visited, candidates_queue)
        # main loop
        current_vertex = v
        while is_valid_candidates:
            # get best candidate
            next_vertex = self._get_best_candidate(visited, candidates_queue)
            # add this candidate vertex to visited
            visited.add(next_vertex)
            # update solution object
            overlap = self.graph.compute_overlap(current_vertex, next_vertex, direction)
            solution.add_id(next_vertex)
            solution.add_overlap(overlap)
            solution.add_sequence(self.graph.oligonucleotides_list[next_vertex].value, overlap)
            # update current vertex with best candidate vertex
            current_vertex = next_vertex
            # create candidates queue for new current vertex
            candidates_queue = self._queue_candidates(current_vertex, direction)
            # check if loop should continue
            is_valid_candidates = self._valid_candidates_left(visited, candidates_queue)
        return solution
    def solve_greedy(self):
        # randomize starting vertex
        start = np.random.randint(self.graph.vertices_no)
        print(start)
        # perform subgreedy for both sides
        left_subgreedy = self.solve_subgreedy(start, 'in')
        right_subgreedy = self.solve_subgreedy(start, 'out')
        # merge
        solution = Solution('bidirectional')
        print(left_subgreedy)
        print(right_subgreedy)
        solution.id_list = left_subgreedy.id_list + right_subgreedy.id_list[1:]
        solution.sequence = left_subgreedy.sequence + right_subgreedy.sequence[1:]
        solution.overlaps = left_subgreedy.overlaps + right_subgreedy.overlaps
        return solution