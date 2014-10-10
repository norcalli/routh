#!/usr/bin/env python

def main(*vector):
  m = len(vector)
  n = (m + 1) // 2
  v = lambda j: float(vector[j]) if 0 <= j < m else 0

  A = [[0 for i in range(n)] for j in range(m)]
  a = lambda i,j: A[i][j] if 0 <= i < m and 0 <= j < n else 0

  print '%dx%d' % (m,n)
  print

  # Initialize first two rows.
  for i in range(n):
    A[0][i] = v( i*2 )
    A[1][i] = v( i*2 + 1 )

  # Do update.
  for j in range(2, m):
    for i in range(n):
      x = a(j-1, 0)
      if x == 0:
        x = 1e-300
      A[j][i] = (x * a(j-2, i+1) - a(j-2, 0) * a(j-1, i+1))/ x

  # Count sign changes
  old_sign = a(0,0)
  change = 0
  for x in A:
    y = x[0]
    sign = 1 if y == 0 else y/abs(y)
    if sign != old_sign:
      change += 1
    old_sign = sign
    print x

  # Check for factoring out s = 0 multiplicities
  # by checking how many tail zeroes there are.
  axis = 0
  for i in range(m-1, -1, -1):
    if v(i) != 0:
      break
    axis += 1

  print
  print '%d on the axis' % (axis,)
  print '%d in the RHP (right half plane)' % (change,)
  print '%d in the LHP (left half plane)' % (m - change - axis - 1,)

import sys

if __name__ == '__main__':
  args = sys.argv[1:]
  if not len(args):
    print 'Usage: %s <coefficients>' % (sys.argv[0],)
    print
    print 'Example:'
    print '  %s 1 4 12 4 3' % (sys.argv[0],)
    sys.exit(1)

  main(*args)
