# Cool.py

Make Python code cooler. 100% coverage. Use and enjoy this code!

## Install

```
pip install cool
```

Or fetch from github

```
pip install git+https://github.com/abersheeran/cool@setup.py
```

## Usage

### Pipe

*Note: as fast as you didn't use F!*

Use pipeline to pass data as a positional parameter to the next function:

```python
from cool import F

range(10) | F(filter, lambda x: x % 2) | F(sum) == 25
```

Or you need to pass multiple parameters through the pipeline:

```python
from cool import FF


def get_data():
    return 1, 2


get_data() | FF(lambda x, y: x + y) == 3
```

Use alias like follow code, you can use `map`/`filter`/`reduce` more conveniently:

```python
from functools import reduce
from cool import F

Filter = F(F, filter)
Map = F(F, map)
Reduce = F(F, reduce)

range(100) | Filter(lambda x: x % 2) | Map(lambda x: x * x) | Reduce(lambda x, y: x + y)
```

### Redirect

Just like the redirection symbol in `Shell`, you can redirect the output to a specified file or `TextIO` object through `>` or `>>`.

*Note: `R` inherits from `functools.partial`.*

```python
from pathlib import PurePath
from cool import R

# Redirect output to specified filepath
R(print, "hello") > PurePath("your-filepath")

# Append mode
R(print, "world") >> PurePath("your-filepath")
```

Redirect to opened file or other streams.

```python
from io import StringIO
from cool import R

with open("filepath", "a+", encoding="utf8") as file:
    R(print, "hello") >> file

out = StringIO("")

R(print, "hello") > out

out.seek(0, 0)
out.read() == "hello\n"
```

Maybe you also want to block the output, just like `> /dev/null`.

```python
from cool import R

R(print, "hello") > None
# Or
R(print, "hello") >> None
```

Note that after the calculation is over, `R` will faithfully return the return value of your function. Try the following example.

```python
from pathlib import PurePath
from cool import F, R


def func(num):
    return range(num) | F(map, lambda x: print(x) or x) | F(sum)


print(R(func, 10) > PurePath("filepath"))
```

### Set Global

Maybe you don't want to use `from cool import F` in every file of the entire project, you can use the following code to set it as a global function, just like `min`/`max`/`sum`.

```python
import cool

cool.set_global(cool.F, cool.FF)
```

Maybe you also want to expose `functools.reduce` to the world, just like `map`/`filter`.

```python
import functools
import cool

cool.set_global(cool.F, cool.FF, functools.reduce)
```
