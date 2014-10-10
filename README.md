# Routh-Hurwitz Method Calculator

# Usage


```bash
Berkeley/EEC128/routh git:master             ⏎ ✱ ◼
 ❯❯❯ ./routh.py
Usage: ./routh.py <coefficients>

Example:
  ./routh.py 1 4 12 4 3
```

Simple script which calculates routh-hurwitz table as shown below.

Just pass the coefficients (only floating for now) as the arguments:

```bash
Berkeley/EEC128/routh git:master
 ❯❯❯ ./routh.py 1 4 3 12 2 0
6x3

[1.0, 3.0, 2.0]
[4.0, 12.0, 0.0]
[0.0, 2.0, 0.0]
[-7.999999999999999e+300, 0.0, 0.0]
[2.0, 0.0, 0.0]
[0.0, 0.0, 0.0]

1 on the axis
2 in the RHP (right half plane)
2 in the LHP (left half plane)
```
