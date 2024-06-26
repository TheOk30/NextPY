freqs = [
    ['La', 55],
    ['Si', 61.74],
    ['Do', 65.41],
    ['Re', 73.42],
    ['Mi', 82.41],
    ['Fa', 87.31],
    ['Sol', 98],
]

OCTABS_NUM = 5

class MusicNotes():

    octave_len = 5

    def __init__(self):
        self._freqs = freqs

    def __iter__(self):
        self._index_octabs = 1
        self._index_freq = -1
        return self
    
    # return current element in iterator
    def __next__(self):
        # raise Exception to stop iteration when out of reach
        if self._index_octabs == OCTABS_NUM and self._index_freq >= len(self._freqs) - 1:
            raise StopIteration
        
        elif self._index_freq >= len(self._freqs) - 1:
            self._index_octabs += 1
            self._index_freq = -1
        
        self._index_freq += 1
        return self._freqs[self._index_freq][1] * 2 ** (self._index_octabs -1)


def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)


if __name__ == "__main__":
    main()
