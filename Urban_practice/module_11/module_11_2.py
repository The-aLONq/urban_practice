import inspect
from pprint import pprint
from collections import  OrderedDict

def introspection_info(obj):
    info = OrderedDict([
        ('type', type(obj)),
        ('attributes', [attr for attr in dir(obj) if not callable(getattr(obj, attr))]),
        ('methods', [attr for attr in dir(obj) if callable(getattr(obj, attr))]),
        ('module', inspect.getmodule(obj))
    ])
    return info

pprint(introspection_info(42))
