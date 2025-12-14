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

def min_prime_factors(n):
  factors = [0] * (n + 1)
  i = 2
  while (i * i < n):
    if (factors[i] != 0):
      i += 1
      continue
    j = 2
    while (i * j <= n):
      if (factors[i * j] == 0):
        factors[i * j] = i
      j += 1
    i += 1
  return factors

def block_sizes(x, factors):
  sizes = []
  if (factors[x] == 0):  # if prime
    sizes += [1]
  else:
    quotient = x // factors[x]
    sizes += [quotient]
    if (quotient % factors[x] != 0):
      sizes += [factors[x]]
  return sizes


max_id = max([r[1] for r in range_list])
max_id_len = len(str(max_id))
factors = min_prime_factors(max_id_len)

invalid_sum = 0
for (left, right) in range_list:
  l0, l1 = len(str(left)), len(str(right))
  l0 = max(l0, 2)  # length-one IDs need not be checked
  for l in range(l0, l1 + 1):
    sizes = block_sizes(l, factors)
    already_added = {}
    for k in sizes:
      generator = 10 ** (k - 1)
      if (l == l0):
        generator = max(generator, int(str(left)[ : k]))
        if (int(str(generator) * (l // k)) < left):
          generator += 1
      max_generator = (10 ** k) - 1
      while (generator <= max_generator):
        cur = int(str(generator) * (l // k))
        if (cur > right):
          break
        if (not already_added.get(cur, False)):
          invalid_sum += cur
          already_added[cur] = True
        generator += 1

print(invalid_sum)
