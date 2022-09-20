## GitHub Actions Practice (intro to CI/CD @ OSAI)
This is a repo to demonstrate the power of GitHub actions.
We have implemented a basic Python calculator ([calculator.py](calculator.py)) incorrectly.
All functions in that file are broken.
There are also some syntax issues to fix . . .

**Steps:**
1. Fork the repo (if you don't know how to fork a repo, see this [page](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)).
2. Edit [calculator.py](calculator.py) to fix the syntax and correctness issues in the code.
3. Push your code to your fork.
4. Make a pull request and hope that you see a little green checkmark (which indicates that the tests pass). If you don't know how to make a pull request, see this [page](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).
5. Repeat as necessary until all tests pass and the linter succeeds.

Note: You should not need to clone this repo; try testing changes via GitHub actions on a fork.