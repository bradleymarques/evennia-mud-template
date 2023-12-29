# Evennia MUD template

[![Coverage badge](https://raw.githubusercontent.com/bradleymarques/evennia-mud-template/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/bradleymarques/evennia-mud-template/blob/python-coverage-comment-action-data/htmlcov/index.html)

A template repository for creating MUDs with [Evennia](https://www.evennia.com/).

## What's included?

- [Evennia](https://www.evennia.com/), obviously
- [Poetry](https://python-poetry.org/) as a package manager
- [pre-commit](https://pre-commit.com/) for enforcing:
  - [Black](https://black.readthedocs.io/en/stable/) for formatting
  - [Pycln](https://hadialqattan.github.io/pycln/#/) for detecting and removing unused imports
  - [isort](https://pycqa.github.io/isort/) for automatically sorting imports
- [Coverage](https://coverage.readthedocs.io/en/7.4.0/)
- GitHub action for running unit tests with coverage
- [GitHub action](https://github.com/marketplace/actions/python-coverage-comment) for posting coverage report on PRs into `main`
- Basic folder structure
- Some useful scripts

## Initial setup

First, copy `.env.example` into a (gitignored) file called `.env`, and change
the settings to your liking:

```sh
cp .env.example .env
```

Then, install pre-commit hooks:

```sh
pre-commit install
```

## Running the game server

```sh
poetry install
poetry shell
evennia migrate
evennia start
```

### What's started?

1. <http://localhost:4000/> - Telnet client
2. <http://localhost:4001/> - The Web portal
3. <http://localhost:4002/> - Websocket endpoint

## Playing the game

There are a few options here:

1. Play through the web portal on <http://localhost:4001/>
2. Install a stand-alone MUD client like [Mudlet](https://www.mudlet.org/)
3. Install a terminal-based MUD client like [Tintin++](http://tintin.mudhalla.net/)

If using a MUD client, connect to `127.0.0.1` port `4000`.

If you use TinTin++, simply run the script:

```sh
./scripts/play.sh
```

## Running Tests

To run all the tests with coverage, run:

```sh
./scripts/test
```

To run only certain tests, you can supply a path or Python dot path:

```sh
evennia test --settings settings.py path.to.my.test.MyTest
```

## Included helpful scripts

- `play.sh`: Simply opens a Tintin++ session to localhost. Requires installing [Tintin++](http://tintin.mudhalla.net/)
- `reset.sh`: Pulls down the Evennia server only, deletes the database and logs, and spins it all up again
- `test.sh`: Runs all tests with coverage
