# How to install

1. Copy `.env.example` to `.env` file, and complete the values

2. - Run `pipenv install`

# How to run
Run `pipenv run python -m techcareback.main`

# Running Tests with coverage
Run
```
pipenv run coverage run --source=techcareback -m pytest tests
pipenv run coverage report
```