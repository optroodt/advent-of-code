import inspect
import pathlib


def load_file(filename=None):
    if filename is None:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = pathlib.Path(module.__file__).name.replace(".py", ".txt")
    path = pathlib.Path(filename)
    with path.open("r") as fh:
        return list(map(str.strip, fh.readlines()))
