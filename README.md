# Advent of Code

<img src="/logo.png?raw=true" align="right">

Source code of my solutions to the [Advent of Code](https://adventofcode.com/) challenges.

## Prerequisites

Python >= 3.7.

## Installation

Clone this repo, and then the usual `pip install -r requirements.txt`.

## Configuration

Either set the following environment variables or copy the `.env.example` file to `.env`:

| Name         | Type | Required? | Default | Description                                                                                                   |
|--------------|------|-----------|---------|---------------------------------------------------------------------------------------------------------------|
| `SESSION_ID` | str  | Yes       |         | Advent of Code session ID cookie value. Can be found in the HTTP requests headers when using your web browser |

## Usage

````shell
$ python run.py year day [level]
````
