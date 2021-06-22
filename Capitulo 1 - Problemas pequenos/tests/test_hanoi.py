from hanoi import Stack, hanoi


def test_hanoi():
    num_discs = 3
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()

    for i in range(1, num_discs + 1):
        tower_a.push(i)

    hanoi(tower_a, tower_c, tower_b, num_discs)
    assert tower_a.container == ()
    assert tower_b.container == ()
    assert tower_c.container == tuple(range(1, num_discs + 1))
