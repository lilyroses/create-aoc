# TODO

- [ ] Add UPDATE feature for existing Advent-of-Code directory
  - [ ] Update missing/empty year folder(s)
  - [ ] Update missing/empty day folder(s)
  - [ ] Update missing/empty solution file(s)
  - [ ] Update missing/empty input file(s)
  - [ ] Fetch input data for empty "input.txt" files (if possible)

- [ ] Add DOWNLOAD PUZZLE DESCRIPTION feature

- [ ] Add TEST CASES feature
   - [ ] Download test cases
   - [ ] Create tests/ dir in each day folder
   - [ ] Create test_solution_1.py and test_solution_2.py that read in main() from their respective solution functions
   - [ ] Create test_input_1.txt and test_input_2.txt

- [ ] Add SOLVE PUZZLE feature
   - [ ] Send answer from command line to site and return result

- [x] Move validate_cookie functionality to separate module

- [x] Add `update_progress.py` tool to allow user to
   supply year, day and solution level (1 or 2) as parameters
   to the `update_progress.py` tool, which will then update
   `progress.json` with the relevant progress markers

- [x] Add `check_progress.py` to print a progress calendar
   showing which days are solved.
  - [x] One "calendar" of 5x5 squares per yearly event.
  - [x] One numbered "square" for each day of that event.
  - [x] Each square holds up to 2 stars to indicate the
   completion of that day's puzzle:; one star (`*`) for
   solving part 1, two stars (`**`) for solving both parts of
   the puzzle, and no stars (``) for no solutions.
  - [x] At the top, the calendar will display a `solved/total`
   ratio (e.g. for 10 out of 200 puzzles solved, the ratio
   would be `10/200`.) Each part of the puzzle counts as one
   "solve"; therefore, each day has a maximum of two
   solutions possible which are added up for the ratio total.

