# Chapter 1: Hello, World!

Write a program to enthusiastically greet the world:

```
$ ./hello.py
Hello, World!
```

The program should also accept a name given as an optional `--name` parameter:

```
$ ./hello.py --name Universe
Hello, Universe!
```

The program should produce documentation for `-h` or `--help`:

```
$ ./hello.py -h
usage: hello.py [-h] [-n str]

Say hello

optional arguments:
  -h, --help          show this help message and exit
  -n str, --name str  The name to greet (default: World)
```

Run `pytest -xv test.py` (or `make test`) to ensure you pass all the tests:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 4 items

test.py::test_exists PASSED                                              [ 25%]
test.py::test_usage PASSED                                               [ 50%]
test.py::test_default PASSED                                             [ 75%]
test.py::test_input PASSED                                               [100%]

============================== 4 passed in 0.41s ===============================
```

Tips:

You can use the [template.py](template.py) file as a jumping off point.

### What is argsparse?

It's a module that comes with the standard python library (does not need to be installed).

Minimal example:

File print_input.py

```python
import argparse

def get_args():
  """Get command-line arguments"""
  parser = argparse.ArgumentParser(description="Prints the word you pass")
  parser.add_argument("--input", type=str, required=True, help="word to print")
  return parser.parse_args()



if __name__ == '__main__':
    args = get_args()
    print(args.input)
```

Will function like this:

```
python print_input.py --input hello
```

prints:

```
hello
```

or:

```
python print_input.py --input world
```

prints:

```
world
```
