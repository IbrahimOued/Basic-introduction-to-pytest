# Using `assert`

```python
assert "loud noises".upper() == "LOUD NOISES"

assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

assert 37 in {
    num
    for num in range(1, 50)
    if num != 1 and not any([num % div == 0 for div in range(2, num)])
}
```
