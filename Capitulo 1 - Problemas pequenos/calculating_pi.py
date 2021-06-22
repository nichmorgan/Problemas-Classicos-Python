# Teste de git

# Leibniz's Formula
def calculating_pi(n_terms: int) -> float:
    numerator = 4.
    denominator = 1.
    operation = 1.
    pi = 0.
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.
        operation *= -1.
    return pi
