from datetime import datetime


# ADVENT OF CODE INFO
ADVENT_OF_CODE_BASE_URL = "https://adventofcode.com"
SESSION_COOKIE_FILE = "cookie.txt"

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
