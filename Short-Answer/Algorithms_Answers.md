#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
    a = 0 # O(1)
    while (a < n * n * n): # O(n)
      a = a + n * n # O(1)

# Runtime: O(n)
# It looks like O(n**3) but `(a < n * n * n)` does not exponentially increase the number of times it loops. It's a checker.

```

b)
```python
    sum = 0 # O(1) = constant
    for i in range(n): # O(n)
      j = 1 # O(1) = constant
      while j < n: # O(log(n))
        j *= 2 # O(1) = constant
        sum += 1 # O(1) = constant

# We can simply disregard constants, and do O(n) * O(log(n)) => runtime O(n log(n))
```


c)
```python
    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
# O(n) It's a single loop recursive function.
```

## Exercise II

A Binary Search should work for this task. Start with the middle floor and drop an egg. If it breaks all floors above can be ignored. Then move your low, mid and high points to test the bottom half. If at the new mid it breaks, you rule out the upper floors and vice versa. Repeat until we find a floor that the egg doesn't break at at and the floor directly above does break.

Best case we could run at O(1). Worst case we'll end up somewhere at O(log(n))