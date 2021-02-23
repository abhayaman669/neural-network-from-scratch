# Numpy neuron

## basics

**1D Array or Vector or list**

```
>>> a = [1, 2, 3, 4]
```

shape of `a` is `(4,)`.

> Shape: size of an list

**2D Array or Matrix or List of list**

```
a = [[1, 2, 3], [4, 5, 6]]
```

shape of `a` here is `(4, 3)`.
also a here is an ***homologous*** i.e. the size of each list under main list will be same.

## Numpy

**Dot Product**

let's say we have two list

```
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
```

here the dot product will be: sum of `a[i] * b[i]` where i is in `range(len(a))`.

here is the numpy function for that

```
>>> numpy.dot(a, b)
```

[click here](https://numpy.org/doc/stable/reference/generated/numpy.dot.html) for more details on numpy dot.