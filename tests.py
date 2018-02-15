import pytest
from injector import inject


def test_basic():

    @inject(b=1)
    def add(a, b):
        return a + b

    assert add(5) == 6
    assert add(a=5) == 6
    with pytest.raises(TypeError):
        add(b=5)
