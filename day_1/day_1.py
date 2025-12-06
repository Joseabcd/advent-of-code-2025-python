import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as f:
    data = f.read().splitlines()


# ------------------------------------------------------------
# Part 1
# ------------------------------------------------------------

dial = 50
password = 0
for s in data:
  dial += int(s.replace("R","").replace("L","-"))
  dial %= 100
  if dial == 0:
    password += 1

print(password)


# ------------------------------------------------------------
# Part 2
# ------------------------------------------------------------


dial = 50
password = 0
for s in data:
  rot = int(s.replace("R","").replace("L","-"))
  if rot >= 0:
    password += rot // 100
    rot %= 100
  else:
    rot = -rot
    password += rot // 100
    rot %= 100
    rot = -rot
  dial_was_zero = (dial == 0)
  dial += rot
  if (dial >= 100) or (dial <= 0 and not dial_was_zero):
    password += 1
  dial %= 100

print(password)

