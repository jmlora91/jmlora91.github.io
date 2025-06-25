# BEGIN: Test Cases
def test_suma_lista():
    assert suma_lista([1, 2, 3]) == 6, "Test case 1 failed"
    assert suma_lista([-1, -2, -3]) == -6, "Test case 2 failed"
    assert suma_lista([0, 0, 0]) == 0, "Test case 3 failed"
    assert suma_lista([1.5, 2.5, 3.5]) == 7.5, "Test case 4 failed"
    assert suma_lista([]) == 0, "Test case 5 failed"
    print("All test cases pass")
# END: