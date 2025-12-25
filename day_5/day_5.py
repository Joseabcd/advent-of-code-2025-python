import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as f:
    data = f.read()

range_specs, ingredient_ids = data.split('\n\n')
ingredient_ids = [int(id) for id in ingredient_ids.split()]
range_list = []
for spec in range_specs.split():
  left, right = spec.split('-')
  left, right = int(left), int(right)
  range_list += [range(left, right + 1)]


# ------------------------------------------------------------
# Part 1
# ------------------------------------------------------------

count = 0
for id in ingredient_ids:
  for r in range_list:
    if id in r:
      count += 1
      break

print(count)


# ------------------------------------------------------------
# Part 2
# ------------------------------------------------------------

