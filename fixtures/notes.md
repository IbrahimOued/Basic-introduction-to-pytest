# Fixtures

* Provide data or state to your tests
* Code re-use
* Similar to use of `.setUp()` in `unittest`
* Fixtures are created through the decoration of a function
* Fixtures are consumed by a test as an argument

Fixture are great idea and can help reduce the chances of making mistakes. However, the use of named arguments magically mapping to a fixture somewhere else fells less pythonic. It can even get worse as there are ways to put those fixtures into differents files for orgnization purpose.

## Built-in fixtures

* `cache`: Cache object that persists between testing sessions
* `capsys`: captures text written to stdout and stderr
* `tempdir`: Creates a temporary directory unique to each test function, passed in as a `os.path` object
* `tmp_path`: Creates a temporary directory unique to each test function, passed in as a `pathlib.Path` object

To see the full list of the built-in fixtures run the command:

```python
pytest --fixtures
```

## Fixtures management

* Pytest automatically looks for a `conftest.py` file
* Global configuration can be done here
* Group fixtures seen by all tests
* Create monkey-patches:
  * Code that over-writes existing library calls
  * Stubs out things that shouldn't be done during a test
  * Database, network, date/time, etc.

We can patch a libray function call with it see an example in `conftest.py`

## Slow tests

* Use the --durations argument to report on your slowest tests

```bash
pytest --durations=3
```
