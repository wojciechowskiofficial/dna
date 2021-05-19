class Solution:
    '''
    Container for algorithms' solutions.
    Stores:
        *direction as int (direction of concatenation)
        *id_list as list
        *sequence as string
        *overlaps as list
    '''
    def __init__(self, direction: str, vertex_value_length: int):
        '''
        id_list is a list of visited vertices in the order of visiting
        sequence is resulting DNA sequence
        overlaps is a list of integers of length equal to no_transitions or len(id_list) - 1
        with it's elements being no overlaping letters between vertices
        '''
        self.direction = direction
        self.vertex_value_length = vertex_value_length
        self._validate_direction()
        self.id_list = list()
        self.sequence = str()
        self.overlaps = list()
    def __str__(self):
        ret = 'IDS \n'
        ret += str(self.id_list)
        ret += '\n'
        ret += 'SEQUENCE \n'
        ret += self.sequence
        ret += '\n'
        ret += 'OVERLAPS \n'
        ret += str(self.overlaps)
        return ret
    def __repr__(self):
        self.__str__()
    def _validate_direction(self):
        if self.direction not in {'in', 'out', 'bidirectional'}:
            raise ValueError('invalid direction')
    def add_id(self, id: int):
        '''
        method for adding vertex id to sef.id_list
        :param id: int new vertex id
        '''
        if self.direction == 'in':
            self.id_list.insert(0, id)
        elif self.direction == 'out':
            self.id_list.append(id)
    def add_overlap(self, overlap: int):
        '''
        method for adding overlap to self.overlaps
        :param overlap: int new overlap
        '''
        if self.direction == 'in':
            self.overlaps.insert(0, overlap)
        elif self.direction == 'out':
            self.overlaps.append(overlap)
    def add_sequence(self, seq: str, overlap: int):
        '''
        method for directional sequence concatenation
        :param seq: str new sequence to be appended
        :param overlap: int overlap
        '''
        if self.direction == 'in':
            self.sequence = seq[:len(seq) - overlap] + self.sequence
        elif self.direction == 'out':
            self.sequence = self.sequence + seq[overlap:]