# Contributing to greet-community

## Set up for development

Clone the repository, enter its folder, and activate a Python 3.11+ virtual environment.
```sh
python -m pip install -e .
```

## Run the tests

```sh
python -c "from greet_community import greet; print(greet('Hee'))"
```
Expected output: `Hello, Hee!`

## Send a change

1. Start from `main`: `git switch main`, then `git switch -c add-usage`.
2. Make a change, stage the changed files, and commit with `git commit -m "Add usage example"`.
3. Push with `git push -u origin add-usage`, then open a pull request from `add-usage` to `main`.
