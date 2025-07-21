# create_aoc.py

"""Create a folder of template files and input data within the current
directory for all existing Advent of Code events. If a valid session
cookie is provided in the "cookie.txt" file, the user's puzzle input
will be downloaded to each day folder.

--- 

## Files and folders created by this script:

- Year folders (`2015/`, etc.): One for each year of Advent of Code
  events (including ongoing.)

- Day folders (`day_01/`, etc.): These reside within the year
  folders. for each past event, there are 25 day folders. For
  ongoing events, the number of day folders corresponds to the number
  of days for which puzzles have already been posted.

- Solution files (`solution_1.py`, `solution_2.py`): One for each part
  of the daily puzzle. These contain boilerplate code including a
  module comment indicating the year, day, and solution part, as well
  as code that reads in the data from `input.txt`. For this reason, it
  is highly recommended to either supply your session cookie within
  `cookie.txt` so the script can download your unique input, or for you
  to copy and paste the data into the `input.txt` files yourself for
  each puzzle.

- Input data file (`input.txt`): If a valid session cookie is provided
  in the "cookie.txt" file, the user's puzzle input will be downloaded
  to each day folder. Otherwise, `input.txt` is created, but left
  blank.

### File Tree

Advent-of-Code/
|__ 2015/
    |__ day_01/
        |__ solution_1.py
        |__ solution_2.py
        |__ input.txt
    |__ day_02/
    ...
    |__ day_25/
...
|__ 202[x]
    |__ day_01/
    ...
    |__ day_[xx]/
"""

import os
import requests
import sys
from datetime import datetime


# ADVENT OF CODE INFO
ADVENT_OF_CODE_BASE_URL = "https://adventofcode.com"
SESSION_COOKIE_FILE = "cookie.txt"


def exit_program(complete=False):
  if complete:
    print("\nComplete.")
  print("\nExiting...")
  sys.exit()


def validate_session_cookie(SESSION_COOKIE_FILE):
  """Validate the session cookie within the SESSION_COOKIE_FILE.

  args: SESSION_COOKIE_FILE (str, path)
  returns: cookie_is_valid (Boolean value)
  """
  cookie_is_valid = False

  # cookie file does not exist
  if not os.path.exists(SESSION_COOKIE_FILE):
    continue_without_cookie_file = input(f"\nError: {SESSION_COOKIE_FILE} does not exist. Puzzle input data will not be downloaded. Continue? (Y/N): ")
    if continue_without_cookie_file.upper() == "Y":
      return cookie_is_valid
    else:
      print("\nExiting...")
      sys.exit()
  
  # cookie file exists
  with open(SESSION_COOKIE_FILE, "r") as f:
    SESSION_COOKIE = f.read().strip()
  
  # cookie file is empty
  if not SESSION_COOKIE:
    continue_without_cookie_text = input(f"\n{SESSION_COOKIE_FILE} does not contain a cookie. Puzzle input data will not be downloaded. Continue? (Y/N): ")
    if continue_without_cookie_text.upper() == "Y":
      return cookie_is_valid
    else:
      exit_program()
    
  # cookie file is not empty
  # Test cookie for validity
  session = requests.Session()
  HEADERS = {
    "Cookie":f"session={SESSION_COOKIE}",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
  }
  test_url = f"{ADVENT_OF_CODE_BASE_URL}/2015/day/1/input"
  response = session.get(test_url, headers=HEADERS)

  # cookie is valid
  if response.status_code == 200:
    cookie_is_valid = True
    return cookie_is_valid

  # cookie is not valid
  if not cookie_is_valid:
    continue_prompt = input("Non-existent or invalid cookie. Puzzle input data will not be downloaded. Continue? (Y/N): ")
    if continue_prompt.upper() != "Y":
      exit_program()
    else:
      return cookie_is_valid

def fetch_input_data(cookie, )


# DATE RANGES
current = datetime.today()
YEAR_START, YEAR_END = (2015, current.year)
if current.month != 12:
  YEAR_END -= 1
YEAR_RANGE = range(YEAR_START, YEAR_END+1)
DAY_START, DAY_END = (1,25)
DAY_RANGE = range(DAY_START, DAY_END+1)

# EVENT STATUS
EVENT_ONGOING = False
MONTH_IS_DECEMBER = current.month == 12
DATE_IS_WITHIN_ADVENT = current.day <= DAY_END
if (MONTH_IS_DECEMBER and DATE_IS_WITHIN_ADVENT):
  EVENT_ONGOING = True
  DAY_RANGE_ADVENT_ONGOING = range(DAY_START, current.day+1)


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
  content = f"""# Solution {solution_number} - Advent of Code {year}, Day {day}

INPUT_FILE = \"input.txt\"
with open(INPUT_FILE, \"r\") as f:
  lines = [line.strip() for line in f.readlines()]


def main():
  pass


if __name__ == \"__main__\":
  main()
"""

  return content


def create_aoc(PROJECT_FOLDER_PATH, YEAR_RANGE, DAY_RANGE):

  # Create Advent-of-Code directory
  create_directory(PROJECT_FOLDER_PATH)

  # Create year folders
  for year in YEAR_RANGE:
    year_folder = f"{year}"
    year_folder_path = os.path.join(PROJECT_FOLDER_PATH, year_folder)
    create_directory(year_folder_path)

    # Create day folders
    if (year == current.year and EVENT_ONGOING):
      DAY_RANGE = DAY_RANGE_ADVENT_ONGOING
    for day in DAY_RANGE:
      day_folder = f"day_{day:02d}"
      day_folder_path = os.path.join(year_folder_path, day_folder) 
      create_directory(day_folder_path)

      # Create solution files
      solution_1_file_path = os.path.join(day_folder_path, SOLUTION_1_FILE_NAME)
      solution_1_file_content = generate_solution_file_content(1, year, day)
      create_file(solution_1_file_path, solution_1_file_content)

      solution_2_file_path = os.path.join(day_folder_path, SOLUTION_2_FILE_NAME)
      solution_2_file_content = generate_solution_file_content(2, year, day)
      create_file(solution_2_file_path, solution_2_file_content)

      input_data_file_path = os.path.join(day_dir, INPUT_DATA_FILE_NAME)
      puzzle_input = ""    
      cookie_is_valid = validate_session_cookie()
      if cookie_is_valid:
        puzzle_input_url = f"{ADVENT_OF_CODE_BASE_URL}/{year}/day/{day}/input"
        session = requests.Session()
        response = session.get(puzzle_input_url, headers=HEADERS)
        if response.status_code == 200:
          puzzle_input = response.text
      with open(input_data_file_path, "w") as f:
        f.write(puzzle_input.strip())

exit_program(complete=True)
