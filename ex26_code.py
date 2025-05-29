import ex26
import sys
from pprint import pprint

print("name", ex26.name)
print("height", ex26.height)
print("height is also", ex26.__dict__['height'])
# pprint(ex26.__dict__)

print(f"I am currently {ex26.height} inches tall.")

ex26.__dict__['height'] = 1000
print(f"I am now {ex26.height} inches tall.")

ex26.height = 12
print(f"Oops, now I'm {ex26.__dict__['height']} inches tall.")


# print(pprint.__doc__)
# this is the same:
# help(pprint)

print(sys.__doc__)

print(sys.__name__)