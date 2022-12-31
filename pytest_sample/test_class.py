"""
Unlike the standard library unittest pytest
doesn't have to inherit anything specific.
Pytest looks for functions or method starting with test.

If you want to group your tests you can do it this way
"""

class SampleClass:
    def test_always_pass(self):
        assert True

    def test_always_fail(self):
        assert False