import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as f:
    data = f.read()

bank_list = data.split()


# ------------------------------------------------------------
# Part 1
# ------------------------------------------------------------

total_jolts = 0
for bank in bank_list:
  p0, p1 = 0, 1
  for p in range(1, len(bank)):
    if bank[p] > bank[p0] and p < (len(bank) - 1):
      p0 = p
      p1 = p0 + 1
    elif bank[p] > bank[p1]:
      p1 = p
      if bank[p1] == '9':
        break
  cur_jolts = int(bank[p0] + bank[p1])
  total_jolts += cur_jolts

print(total_jolts)


# ------------------------------------------------------------
# Part 2
# ------------------------------------------------------------

