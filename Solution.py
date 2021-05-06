class Solution:
    '''
    Container for algorithms' solutions.
    Stores:
        *direction as int (direction of concatenation)
        *id_list as list
        *sequence as string
        *overlaps as list
    '''
    def __init__(self, direction: str):
        '''
        id_list is a list of visited vertices in the order of visiting
        sequence is resulting DNA sequence
        overlaps is a list of integers of length equal to no_transitions or len(id_list) - 1
        with it's elements being no overlaping letters between vertices
        '''
        self.direction = direction
        self._validate_direction()
        self.id_list = list()
        self.sequence = str()
        self.overlaps = list()
    def _validate_direction(self):
        if self.direction not in {'left', 'right'}:
            raise ValueError('invalid direction')
    def add_id(self, id: int):
        '''
        method for adding vertex id to id_list
        :param id: int new vertex id
        '''
        if self.direction == 'left':
            self.id_list.insert(0, id)
        elif self.direction == 'right':
            self.id_list.append(id)
    def concatenate_sequence(self, seq: str, overlap: int, direction: str):
        '''
        method for directional sequence concatenation
        :param seq: str new sequence to be appended
        :param overlap: int overlap
        :param direction: str 'right' or 'left'
        '''
        # TODO: not done - implement
        if direction == 'right':
            self.sequence = self.sequence + seq[overlap]
        elif direction == 'left':
            self.sequence = seq[:len(seq) - overlap] + self.sequence
    def add_overlap(self, current: int, next: int, direction: str):
        '''
        method for adding overlap
        :param metric: int metric value / arc value
        '''
        # TODO: not done - implement
        pass