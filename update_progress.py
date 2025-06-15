import os
import sys

from data import project_data
from data import progress_data


PROGRESS_DATA = progress_data.PROGRESS_DATA
PROGRESS_DATA_FILE = os.path.join(os.getcwd(), "data", "progress_data.py")

args = sys.argv
if len(args) != 3:
  print(f"\nError: Expected 3 arguments (year, day, solution_part).")
  sys.exit()

year, day, solution_part = args

try:
  year = int(year)
exacept ValueError:
  print(f"\nError: Parameters must be numeric (year, day, solution_part).")
  sys.exit()

try:
  day = int(day)
except ValueError:
  print(f"\nError: Parameters must be numeric (year, day, solution_part)."
  sys.exit()

try:
  solution_part = int(solution_part)
except ValueError:
  print(f"\nError: Parameters must be numeric (year, day, solution_part)")
  sys.exit()

if year not in project_data.YEAR_RANGE:
  


def update_progress_data(year, day, level):
  pass

#with open(PROGRESS_DATA_FILE, "w") as f:
#  f.write(PROGRESS_DATA)

