# injector

Dependency injection for Python 3.3+

Use injector to bind values to transparently bind parameters to functions
and update the call function's call signature to match.


### Installation
Requirements:

    python 3.3+

Install using `pip`:

    pip install https://github.com/olirice/injector.git 

### Basic Usage

    >>> from injector import inject
    >>> @inject(b=1)
    >>> def add(a, b):
    >>>     return a + b
    >>>
    >>> add(5)
    6
    >>> add(a=5)
    6
    >>> add(b=5)
    TypeError: add() missing 1 required positional argument: 'a'

