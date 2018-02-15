# coding: utf-8

from inspect import signature
from functools import wraps
from typing import Callable


__version__ = '1.0.0'


class ComponentInitializer:
    """Wraps an initializer function for an injected component"""

    def __init__(self, component_initializer: Callable):
        self.component_initializer = component_initializer


    def initialize_component(self):
        """Initialize the component to inject"""
        return self.component_initializer()


def inject(**inject_map):
    """Decorator factory that injects variables by name

    If the user passes an injected parameter as a kwarg then
    the user-defined value takes precedent (for ease of testing)
    """
    # TODO(OR): Check compatibility with *args

    def decorator(func):
        ###
        # Runs when function is defined
        ###

        # Original function signature
        sig = signature(func)

        # Remove any positional named arguments we just injected from the signature
        # Inject by name
        altered_params = tuple(v for v in sig.parameters.values()
                               if v.name not in inject_map.keys())

        # Update wrapper signature
        wrapper_sig = sig.replace(parameters=altered_params)

        @wraps(func)
        def wrapper(*args, **kwargs):
            ###
            # Runs for each request
            ###
            args_to_kwargs = dict((p.name, arg) for p, arg in zip(altered_params, args))

            # Merge injected args, positional args (converted to kwargs), and passed kwargs
            params_as_kwargs = {}
            params_as_kwargs.update(inject_map)
            params_as_kwargs.update(args_to_kwargs)
            params_as_kwargs.update(kwargs)

            # Initialize any components wrapped in a ComponentInitializer
            params_as_kwargs = dict((k, v.initialize_component())
                                    if isinstance(v, ComponentInitializer) else (k, v)
                                    for k, v in params_as_kwargs.items())

            # Now that all parameters are stored as kwargs, call the function
            return func(**params_as_kwargs)

        # Override signature
        wrapper.__signature__ = wrapper_sig

        return wrapper
    return decorator
