import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as f:
    data = f.read()

mask = [[int(c.replace('@', '1').replace('.', '0')) for c in line] for line in data.split()]

def accessible_rolls(mask, remove_in_place=False):
  accessible_count = 0
  m, n = len(mask), len(mask[0])
  for i in range(m):
    for j in range(n):
      if mask[i][j]:
        adjacent_count = 0
        if i > 0:
          adjacent_count += mask[i - 1][j]
          if j > 0:
            adjacent_count += mask[i - 1][j - 1]
          if j < n - 1:
            adjacent_count += mask[i - 1][j + 1]
        if i < m - 1:
          adjacent_count += mask[i + 1][j]
          if j > 0:
            adjacent_count += mask[i + 1][j - 1]
          if j < n - 1:
            adjacent_count += mask[i + 1][j + 1]
        if j > 0:
          adjacent_count += mask[i][j - 1]
        if j < n - 1:
          adjacent_count += mask[i][j + 1]
        if adjacent_count < 4:
          accessible_count += 1
          if remove_in_place:
            mask[i][j] = 0
  return accessible_count


# ------------------------------------------------------------
# Part 1
# ------------------------------------------------------------

print(accessible_rolls(mask))


# ------------------------------------------------------------
# Part 2
# ------------------------------------------------------------

total_accessible_rolls = 0
while (current_accessible_rolls := accessible_rolls(mask, remove_in_place=True)):
  total_accessible_rolls += current_accessible_rolls
print(total_accessible_rolls)

