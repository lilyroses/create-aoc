# TODO

- [ ] Add feature to update existing Advent-of-Code directory
  - [ ] Update missing year or day folders
  - [ ] Update missing or empty solution or input files
  - [ ] Fetch input data for empty "input.txt" files (if possible)

- [ ] Add `update_progress.py` tool to allow user to
   supply year, day and solution level (1 or 2) as parameters
   to the `update_progress.py` tool, which will then update
   `progress.json` with the relevant progress markers

- [ ] Add `check_progress.py` to print a progress calendar
   showing which days are solved.
  - [ ] One "calendar" of 5x5 squares per yearly event.
  - [ ] One numbered "square" for each day of that event.
  - [ ] Each square holds up to 2 stars to indicate the
   completion of that day's puzzle:; one star (`*`) for
   solving part 1, two stars (`**`) for solving both parts of
   the puzzle, and no stars (``) for no solutions.
  - [ ] At the top, the calendar will display a `solved/total`
   ratio (e.g. for 10 out of 200 puzzles solved, the ratio
   would be `10/200`.) Each part of the puzzle counts as one
   "solve"; therefore, each day has a maximum of two
   solutions possible which are added up for the ratio total.

