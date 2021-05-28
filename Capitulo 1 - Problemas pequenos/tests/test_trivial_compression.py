import random
from sys import getsizeof

from trivial_compression import CompressedGene


def test_trial_compression():
    original = "".join(random.choice("ACGT") for _ in range(300))
    compressed = CompressedGene(original)

    print(f"Original: {getsizeof(original)}", f"Compressed: {getsizeof(compressed)}")

    assert getsizeof(original) > getsizeof(compressed)
    assert original == compressed.decompress()
