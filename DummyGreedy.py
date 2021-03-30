from Graph import Graph
from Solution import Solution
from random import randint

class DummyGreedy:
    '''
    Primitive Greedy algorithm, which assumes no errors whatsoever.
    pseudocode:
        1. randomly chose non-negative arcs without replacement from graph matrix
        2. start a DNA sequence with the value corresponding to row-vertex of chosen arc
        3. mark that vertex as visited
        4. go to the first non-identical vertex through the arc with the highest value, which was not already visited
        5. append current vertex's value to the DNA sequence
        6. repeat steps 3 to 5 until there are no available non-visited, non-negative vertices to be visited
        7. return DNA sequence
    '''
    def __init__(self, graph: Graph):
        self.graph = graph
        self.solution = Solution()
    def _merge_with_overlap(self, a: str, b: str, overlap: int):
        return a[:len(a) - overlap] + b
    def solve(self):
        '''
        method for running the algorithm
        '''
        i = randint(0, self.graph.vertices_no - 1)
        visited = [i]
        self.solution.sequence = self.graph.oligonucleotides_list[i].value
        self.solution.id_list.append(i)
        neighbour_weights = self.graph.get_vertex_neighbours(i)
        i = neighbour_weights.index(max(neighbour_weights))
        overlap = self.graph.vertex_value_length - max(neighbour_weights)
        if set(neighbour_weights) != {-1}:
            while set(neighbour_weights) != {-1}:
                visited.append(i)
                self.solution.overlaps.append(overlap)
                self.solution.sequence = self._merge_with_overlap(self.solution.sequence, self.graph.oligonucleotides_list[i].value, overlap)
                self.solution.id_list.append(i)
                neighbour_weights = self.graph.get_vertex_neighbours(i)
                i = neighbour_weights.index(max(neighbour_weights))
                if i in visited:
                    break
                else:
                    overlap = self.graph.vertex_value_length - max(neighbour_weights)
