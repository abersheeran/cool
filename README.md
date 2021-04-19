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

assert range(10) | F(filter, lambda x: x % 2) | F(sum) == 25
```

Or you need to pass multiple parameters through the pipeline:

```python
from cool import FF

assert (1, 2) | FF(lambda x, y: x + y) == 3
```

You can use `...` as a placeholder. This is useful when you need to pass non-continuous parameters to create a partial function.

```python
from functools import reduce
from cool import F

assert range(10) | F(reduce, lambda x, y: x + y) == 45
assert range(10) | F(reduce, lambda x, y: x + y, ..., 10) == 55

square = F(pow, ..., 2)
assert range(10) | F(map, square) | F(sum) == 285
```

The `range(10) | F(reduce, lambda x, y: x + y, ..., 10)` is equivalent to `reduce(lambda x, y: x + y, range(10), 10)`.

### Compose functions

*Inspired by [F# function-composition-and-pipelining](https://docs.microsoft.com/en-us/dotnet/fsharp/language-reference/functions/#function-composition-and-pipelining).*

Combine two functions to generate a new function.

```python
from cool import C, F

nonlazy_map = map >> C(list)

assert range(10) | F(nonlazy_map, lambda x: x * x) == [i * i for i in range(10)]
```

Of course, you can also use CC to pass multiple parameters.

```python
import functools
from cool import CC, F

reduce = (
    (lambda a0, a1, a2=None: (a0, a1) if a2 is None else (a0, a2, a1))
    >> CC(functools.reduce)
)
assert range(10) | F(reduce, lambda x, y: x + y) == 45
assert range(10) | F(reduce, lambda x, y: x + y, 55) == 100
```

Maybe you don't understand the meaning of this operator. So let me give two examples.

```
t = f >> C(g)
y = t(x)

# Equivalent to

y = g(f(x))
```

```
t = f >> CC(g)
y = t(x)

# Equivalent to

y = g(*f(x))
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
assert out.read() == "hello\n"
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
