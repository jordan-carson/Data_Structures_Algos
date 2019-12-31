# Week 2

Why is coming up with a good algorithm important?

1. Problem Statement -> Algorithm
2. Fibonacci Numbers

Fn =
```
     {
        0             -> n=0
        1             -> n = 1
        Fn-1 + Fn-2   -> N > 1
     }
```

```python
def FibRecurs(n):
    if n <= 1:
        return n
    else:
        return FibRecurs(n - 1) + FibRecurs(n - 2)
```