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
import tempfile

from event_info import *
from validate_session_cookie import get_session_cookie, validate_session_cookie


# PROJECT PATH INFO
cwd = os.getcwd()
parent_dir = os.path.dirname(cwd)
SESSION_COOKIE_FILE = "cookie.txt"



def exit_program(complete=False):
    """Exits the program with a message."""
    if complete:
        print("\nComplete.")
    print("\nExiting...")
    sys.exit()


def check_dir_is_writeable(project_dir_name):
    """Ensure that the Advent-of-Code/ project directory is writable.

    Args:
      * project_dir_name: the directory name where the Advent-of-Code/
        folder will be created, which by default is the parent
        directory of the create-aoc/ folder. (str)

    Return value:
      * dir_is_writeable: a Boolean value representing whether or not
        the project directory is writeable. (bool)
    """
    try:
        # avoid name clashes
        testfile = tempfile.TemporaryFile(dir=dir_name)
        testfile.close()
    except OSError as e:
        print(f"Error: {project_dir_name} is not writeable.")
        return False
    else:
        return True


def fetch_input_data(cookie, input_data_url, input_data_path):
    pass


# FILE & FOLDER CREATION
def create_directory(dir_path):
    pass


def create_file(file_path, contents=""):
    pass


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


project_dir_is_writeable = check_dir_is_writeable(parent_dir)
if not project_dir_is_writeable:
    exit_program(complete=False)

project_dir = parent_dir


session_cookie = get_session_cookie(SESSION_COOKIE_FILE)
if not session_cookie:
    continue_without_cookie = input(f"\nError: session cookie does not exist. Puzzle input data will not be downloaded. Continue? (Y/N): ")
    if continue_without_cookie_file.upper() != "Y":
        print(f"Update your {SESSION_COOKIE_FILE} with your logged in session cookie and re-run create_aoc.py.")
        sys.exit(complete=False)

cookie_is_valid = validate_session_cookie(session_cookie)
if not cookie_is_valid:
    pass