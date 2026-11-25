from test_sum import test_list


def test_tuple():
    assert sum((1, 2, 2)) == 6, "Expected 6"


if __name__ == "__main__":
    test_list()
    test_tuple()
