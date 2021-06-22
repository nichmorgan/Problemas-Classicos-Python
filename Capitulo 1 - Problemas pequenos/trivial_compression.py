class IntWrapper(int):
    def __getitem__(self, item: int) -> str:
        return self[item]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self) -> int:
        bit_index = 0 + (self._index - 1) * 2
        if bit_index < self.bit_length():
            item = self >> bit_index & 0b11
            self._index += 1
            return item
        else:
            raise StopIteration


class CompressedGene:
    bit_string: IntWrapper

    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: IntWrapper = IntWrapper(1)  # começa com um sentinela
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # desloca dois bits para a esquerda
            if nucleotide == "A":  # muda os dois últimos bits para 00
                self.bit_string |= 0b00
            elif nucleotide == "C":  # muda os dois últimos bits para 01
                self.bit_string |= 0b01
            elif nucleotide == "G":  # muda os dois últimos bits para 10
                self.bit_string |= 0b10
            elif nucleotide == "T":  # muda os dois últimos bits para 11
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide: {nucleotide}")

    def decompress(self) -> str:
        gene: str = ""
        for bits in self.bit_string:
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid bits: {bits}")
        return gene[::-1]  # [::-1] invert a string usando fatiamento com inversão

    def __str__(self) -> str:
        return self.decompress()
