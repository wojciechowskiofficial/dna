class Vertex:
    '''
    Container for oligonulceotides
    '''
    def __init__(self):
        self.value = str()
        self.id = int()
    def __str__(self):
        return '[id: ' + str(self.id) + ' value: ' + self.value + ']'
    def __repr__(self):
        return self.__str__()