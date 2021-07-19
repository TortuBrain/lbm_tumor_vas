import taubrain as tb


def test_tortusity_geometric_value_zero():
    assert tb.tortuosity.tortuosity_geometric([]) == 0
