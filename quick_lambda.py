

class QL:
  def __add__(self, other):
    return lambda x: x + other
  def __sub__(self, other):
    return lambda x: x - other
  def __mul__(self, other):
    return lambda x: x * other
  def __div__(self, other):
    return lambda x: x / other
  def __bitor__(self, other):
    return lambda x: x | other
 

class DoubleQL:
  def __add__(self, other):
    return lambda x, y: (x + other, y + other)
  def __sub__(self, other):
    return lambda x, y: (x - other, y - other)
  def __mul__(self, other):
    return lambda x, y: (x * other, y * other)
  def __div__(self, other):
    return lambda x, y: (x / other, y / other)
  def __bitor__(self, other):
    return lambda x, y: (x | other, y | other)
 

_1 = DoubleQL
_2 = DoubleQL
_1_1 = DoubleQL
