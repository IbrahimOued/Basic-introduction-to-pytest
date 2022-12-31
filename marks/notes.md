# `MARKS`

* Name and group your tests
* Execute just those tests with a given mark
* Built-in marks come with Pytest

Marking a function requires 2 things:

* A decorator to indicate the mark on the test function
* Register the mark

We can apply multiple decorators marks on a function so it can be a member of multiple groups.

It's a common usage to set a **smoke test** (set of tests that can be run in a short amount of time but provide a decent coverage) and a **regression test** (a full coverage and take longer)

Pytest requires us to register our marks in a `pytest.ini` file

## Here are some built-in marks

* `skip`: skips a test
* `skipif`: skips a test if the accompanying expression is `True`
* `xfail`: mark that the test expected to fail, suite will pass if it does

To see the full list of the built-in markers run the command:

```bash
pytest --markers
```
