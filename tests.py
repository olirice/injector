import pytest
from injector import inject, ComponentInitializer


def test_basic():

    @inject(b=1)
    def add(a, b):
        return a + b

    assert add(5) == 6
    assert add(a=5) == 6
    with pytest.raises(TypeError):
        add(b=5)


def test_component_initializer():

    def build_my_component():
        """Initializer function that builds some component"""
        return 5

    @inject(b=ComponentInitializer(build_my_component))
    def add(a, b):
        return a + b

    assert add(5) == 10
