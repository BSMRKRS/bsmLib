# hidePrints

Hides print to console called by any function using `with` statement.

## Example

```python
from bsmLib import hidePrints

with hidePrints():
    x = 1
    print("Hello") # Won't print

# Will print
print(x)
print("Good Bye")
```
