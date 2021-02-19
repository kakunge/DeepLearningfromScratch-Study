import contextlib
from set import *

#with 문 사용

@contextlib.contextmanager
def config_test():
    print('start')
    try:
        yield
    finally:
        print('done')
    
with config_test():
    print('process...')

#모드 전환 구현

@contextlib.contextmanager
def using_config(name, value):
    old_value = getattr(Config, name)
    setattr(Config, name, value)
    try:
        yield
    finally:
        setattr(Config, name, old_value)

with using_config('enable_backprop', False):
    x = Variable(np.array(2.0))
    y = square(x)

def no_grad():
    return using_config('enable_backprop', False)

with no_grad():
    x = Variable(np.array(2.0))
    y = square(x)