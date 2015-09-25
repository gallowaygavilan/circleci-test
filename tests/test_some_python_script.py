from some_python_script import *

def test_add_numbers():
    assert add_numbers(2, 3)  == 5

def test_divide_numbers():
    assert divide_numbers(10, 5) == 2

def test_fails():
    assert divide_numbers(10, 5) == 3
