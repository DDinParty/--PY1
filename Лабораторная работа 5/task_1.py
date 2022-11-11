# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
list_new = range(0, 16)
list___ = [{'bin': bin(o), 'dec': o, 'hex': hex(o), 'oct': oct(o)} for o in list_new]
pprint(list___)
