import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as f:
    data = f.read()

range_list = [tuple(int(e) for e in r.split("-")) for r in data.split(",")]


# ------------------------------------------------------------
# Part 1
# ------------------------------------------------------------

def is_invalid(id0):
  s = str(id0)
  n = len(s)
  return s[ : (n // 2)] == s[(n // 2) : ]

def next_invalid(id0):
  s = str(id0)
  n = len(s)
  if (n % 2 != 0):
    first_half = 10 ** (n // 2)
  else:
    first_half = int(s[ : (n // 2)])
    second_half = int(s[(n // 2) : ])
    if (second_half >= first_half):
      first_half += 1
  s_next = str(first_half) + str(first_half)
  return int(s_next)


invalid_sum = 0
for (left, right) in range_list:
  if (is_invalid(left)):
    invalid_sum += left
  cur = next_invalid(left)
  while (cur in range(left, right + 1)):
    invalid_sum += cur
    cur = next_invalid(cur)

print(invalid_sum)


# ------------------------------------------------------------
# Part 2
# ------------------------------------------------------------

