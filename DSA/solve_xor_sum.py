"""
Problem: Given x + y = a and x ^ y = b, find 2x + 3y for the smallest x.

Key identity: x + y = (x ^ y) + 2 * (x & y) (carryless sum + carry bits)
Therefore:   x & y = (a - b) / 2 (substitute defs of a, b into identity)

Bits split into two groups:
  - (x & y) bits: both x and y have a 1 — forced
  - (x ^ y) bits: exactly one of x, y has a 1 — our choice
  - 

To minimize x, assign all XOR bits to y (ones that need to be 1 where other is 0)
Essentially same as x & y, basically assign x to only where it NEEDS to be 1
  x = (a - b) // 2
Now, since x is 0 where y is 1 to produce 1 in b (x NEVER 1 where b is 1 due to assignment)
  y = x | b (acts as trivial addition)

Validity requires:
  - a >= b (can't have more differing bits than the sum)
  - (a - b) is even (carries must be whole bits)
  - ((a - b) // 2) & b == 0 (carry bits and XOR bits can't overlap)
"""


def solve(a, b):
  # validity checks 1 and 2: x cannot be negative and 
  # we must have 
  if a < b or (a-b) % 2 == 1: return None

  x = (a - b) // 2 # bits that produce the carry ONLY
  y = x | b # addition to get other bits

  # carry bits and other bits cannot overlap, otherwise we're good!
  if ((a - b) // 2 & b != 0):
    return None
  else:
    return 2*x + 3*y



if __name__ == "__main__":
    print(solve(139, 75))  # 385
