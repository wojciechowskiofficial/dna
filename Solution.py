class Solution:
    '''
    Container for algorithms' solutions.
    Stores:
        *id_list as list
        *sequence as string
        *overlaps as list
    '''
    def __init__(self):
        '''
        id_list is a list of visited vertices in the order of visiting
        sequence is resulting DNA sequence
        overlaps is a list of integers of length equal to no_transitions or len(id_list) - 1
        with it's elements being no overlaping letters between vertices
        '''
        self.id_list = list()
        self.sequence = str()
        self.overlaps = list()