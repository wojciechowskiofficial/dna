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
    def concatenate_sequence(self, seq: str, metric: int, direction: str):
        '''
        method for directional sequence concatenation
        :param seq: str new sequence to be appended
        :param metric: int metric value / arc value
        :param direction: str 'right' or 'left'
        '''
        overlap = self._compute_overlap(metric)
        if direction == 'right':
            self.sequence = self.sequence + seq[overlap]
        elif direction == 'left':
            self.sequence = seq[:len(seq) - overlap] + self.sequence
    def add_overlap(self, current: int, next: int, direction: str):
        '''
        method for adding overlap
        :param metric: int metric value / arc value
        '''
        pass