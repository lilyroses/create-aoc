import os
import requests
import sys
from datetime import datetime


# ADVENT OF CODE INFO
ADVENT_OF_CODE_BASE_URL = "https://adventofcode.com"
SESSION_COOKIE_FILE = "cookie.txt"
with open(SESSION_COOKIE_FILE, "r") as f:
  SESSION_COOKIE = f.read().strip()
# Cookie key will be removed if cookie is invalid or missing
HEADERS = {
  "Cookie":f"session={SESSION_COOKIE}",
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


def validate_session_cookie(SESSION_COOKIE):
  if not SESSION_COOKIE:
    cookie_is_valid = False
  # Test cookie for validity
  else:
    session = requests.Session()
    test_url = f"{ADVENT_OF_CODE_BASE_URL}/2015/day/1/input"
    response = session.get(test_url, headers=HEADERS)
    if response.status_code == 200:
      cookie_is_valid = True
    else:
      cookie_is_valid = False

  if not cookie_is_valid:
    continue_prompt = input("Non-existent or invalid cookie. Continue? Puzzle input data will not be downloaded. (Y/N): ")
    if continue_prompt.upper() != "Y":
      exit_program()
  else:
    return cookie_is_valid

cookie_is_valid = validate_session_cookie(SESSION_COOKIE)
if not cookie_is_valid:
  del HEADERS["Cookie"]


# DATE RANGES
current = datetime.today()

YEAR_START = 2015
YEAR_END = current.year
if current.month != 12:
  YEAR_END -= 1
YEAR_RANGE = range(YEAR_START, YEAR_END+1)

DAY_START = 1
DAY_END = 25
DAY_RANGE = range(DAY_START, DAY_END+1)

EVENT_ONGOING = False
if current.month == 12 and current.day <= DAY_END:
  EVENT_ONGOING = True


# FILE AND FOLDER NAMES
CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(os.getcwd())

PROJECT_FOLDER_NAME = "Advent-of-Code"
PROJECT_FOLDER_PATH = os.path.join(PARENT_DIR, PROJECT_FOLDER_NAME)

SOLUTION_1_FILE_NAME = "solution_1.py"
SOLUTION_2_FILE_NAME = "solution_2.py"
INPUT_DATA_FILE_NAME = "input.txt"


# FILE & FOLDER CREATION
def create_directory(dir_path):
  if os.path.exists(dir_path):
    if os.listdir(dir_path):
      print(f"\nError: {dir_path} exists and is non-empty.")
      exit_program()
    else:
      print(f"\n{dir_path} exists and is empty. Continuing setup...")
  else:
    try:
      os.mkdir(dir_path)
    except FileNotFoundError:
      print(f"\nError: Incorrect path for {dir_path}. Ensure all directories exist before continuing.")
      exit_program()
    except OSError:
      print("\nError: Permission denied when attempting creation of {dir_path}.")
      exit_program()


def create_file(file_path, contents=""):
  if os.path.exists(file_path):
    print(f"\nError: {file_path} exists.")
    exit_program()
  else:
    try:
      with open(file_path, "w") as f:
        f.write(contents)
    except OSError:
      print(f"\nError: Permission denied when attempting to write {file_path}.")
      exit_program()
    except FileNotFoundError:
      print(f"\nError: Incorrect path for {file_path}. Ensure all directories exist before continuing.")
      exit_program()

def generate_solution_file_content(solution_number, year, day):
  content = f"""# Solution 1 - Advent of Code {year}, Day {day}

INPUT_FILE = \"input.txt\"
with open(INPUT_FILE, \"r\") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  pass


if __name__ == \"__main__\":
  main()
"""

  return content


create_directory(PROJECT_FOLDER_PATH)

for year in YEAR_RANGE:
  year_dir = os.path.join(PROJECT_FOLDER_PATH, f"{year}")
  create_directory(year_dir)
  if year == current.year and current.month == 12 and current.day < 25:
    DAY_RANGE = range(1, current.day+1)
  for day in DAY_RANGE:
    day_dir = os.path.join(year_dir, f"day_{day:02d}")
    create_directory(day_dir)

    solution_1_path = os.path.join(day_dir, SOLUTION_1_FILE_NAME)
    solution_1_content = generate_solution_file_content(1, year, day)
    create_file(solution_1_path, solution_1_content)

    solution_2_path = os.path.join(day_dir, SOLUTION_2_FILE_NAME)
    solution_2_content = generate_solution_file_content(2, year, day)
    create_file(solution_2_path, solution_2_content)

    input_data_file_path = os.path.join(day_dir, INPUT_DATA_FILE_NAME)
    puzzle_input = ""
    if cookie_is_valid:
      puzzle_input_url = f"{ADVENT_OF_CODE_BASE_URL}/{year}/day/{day}/input"
      session = requests.Session()
      response = session.get(puzzle_input_url, headers=HEADERS)
      if response.status_code == 200:
        puzzle_input = response.text
    with open(input_data_file_path, "w") as f:
      f.write(puzzle_input.strip())

print("\nComplete.")
