# create-aoc
Create folders and template files (for Python) for each year and day of Advent of Code events. When a valid session cookie is provided in `cookie.txt`, the script will download your personal puzzle inputs as well.

## Files in This Repository
- `create-aoc.py` : Generates files and folders for solving Advent of Code puzzles. For each year of AoC events (2015-latest event), a folder is created, e.g. `2015/`. Within each of those folders, 25 `day_xx` folders are created, with the exception of ongoing AoC events: if the month is December and the event is not yet over (e.g. the day of the month is < 25), then only folders up to and including the current day are created.

- `cookie.txt` : An empty file where you can store your logged in session cookie for your Advent of Code account, so that the script can download all your puzzle data for you.

## Generated Files and Directories
The directory layout created by this script is as follows:

```
Advent-of-Code/
|__ 2015/
   |__ day_01/
      |__ solution_1.py
      |__ solution_2.py
      |__ input.txt
  ...
  |__ day_25/
...
|__ 202x/
    ...
```

The file templates are for solving the puzzles in Python. 

- `solution_1.py` and `solution_2.py` both contain the following Python boilerplate (the year, day, and solution number change accordingly).

```# Solution 1 - Advent of Code 2024, Day 1

INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]

def main():
  pass


if __name__ == "__main__":
  main()
```

- `input.txt` remains empty unless a valid session cookie is provided, in which case it will download your personal puzzle input for each Advent of Code puzzle.
