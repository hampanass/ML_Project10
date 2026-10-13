from preprocessing import normalize

def test_normalize():
    assert normalize([10, 20, 30]) == [0.0, 0.5, 1.0]
