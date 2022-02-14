def sort_pair(a, b):
    if a <= b:
        result = a, b  # error
    else:
        result = b, a
    return result


def test_sort_pair():
    a, b = sort_pair(1, 2)
    assert a == 1 and b == 2

    a, b = sort_pair(2, 1)
    assert a == 1 and b == 2

    a, b = sort_pair(1, 1)
    assert a == 1 and b == 1

# C0:  statements
# C1:  branches
# C2:  paths
#   C2a:  all paths
#   C2b:  all paths, with loop run through and continue
#   C2c:  all paths, with n ε N loop runs
# C3:  conditions
#   C3a:  each sub-condition tested with true and false
#   C3b:  all combinations of sub-conditions tested
#   C3c:  each condition tested as one with true and false
