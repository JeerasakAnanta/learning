# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4
    assert func(-1) == 0
    assert func(0) == 1
    assert func(100) == 101     

