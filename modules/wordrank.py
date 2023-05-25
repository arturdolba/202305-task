'''
Contains class for counting and ranking words.
'''

class WordRank:
    '''
    Counts and rank words frequency.

    Needs call constructor with list of words and limit of rank, e.g.:
    r = WordRank(words : list, top: int)
    where:
     - words: is list of str, representing all words in document
     - top: is int, tells how much n-th most frequent records do we need. 
    
    Results can be reached by calling:
    r.get_results()
    '''
    words = []
    limit = []
    _counter = {}
    _rank = []
    def __init__(self, words, limit):
        self.words = words
        self.limit = limit
        self._counter = {}

    def _count_words(self):
        for word in self.words:
            try:
                self._counter[word] += 1
            except KeyError:
                self._counter[word] = 1

    def _generate_rank(self):
        limit = self.limit
        counter_length = len(self._counter)
        if counter_length < limit:
            limit = counter_length
        self._rank = [[k, v] for k, v in self._counter.items()]
        self._rank = sorted(self._rank, key=lambda item: (-item[1], item[0]))[:limit]


    def get_result(self):
        '''
        Returns results - most frequent words.
        '''
        self._count_words()
        self._generate_rank()
        return self._rank
