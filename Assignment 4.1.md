
1.Write a function so that the columns of the output matrix are powers of the input
vector.
The order of the powers is determined by the increasing boolean argument. Specifically,
when increasing is False, the i-th output column is the input vector raised element-wise
to the power of N - i - 1.


```python
import numpy as np
```


```python
x = np.array([1, 2, 3, 5])
```


```python
N = 3
```


```python
np.vander(x, N)
```




    array([[ 1,  1,  1],
           [ 4,  2,  1],
           [ 9,  3,  1],
           [25,  5,  1]])




```python
 np.vander(x, increasing=False)
```




    array([[  1,   1,   1,   1],
           [  8,   4,   2,   1],
           [ 27,   9,   3,   1],
           [125,  25,   5,   1]])




```python
 np.vander(x, increasing=True)
```




    array([[  1,   1,   1,   1],
           [  1,   2,   4,   8],
           [  1,   3,   9,  27],
           [  1,   5,  25, 125]])




```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
