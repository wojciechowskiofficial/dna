from Graph import Graph
from Solution import Solution

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
    def solve(self):
        '''
        method for running the algorithm
        :return: Solution object
        '''
        print(self.graph)