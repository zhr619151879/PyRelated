import contextlib
@contextlib.contextmanager
def name_error():
    try:
        yield
    except NameError as e:
        print(f'name_error found exception! :{e}')

with name_error() as x :
    if name == 2:
        print(1)