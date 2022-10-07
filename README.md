# Advent of Code

Source code of my solutions to the [Advent of Code](https://adventofcode.com/) challenges.

## Prerequisites

Python >= 3.7.

## Installation

Clone this repo, and then the usual `pip install -r requirements.txt`.

## Configuration

Copy the `.env.example` file to `.env` and fill in the configuration parameters:

| Name         | Type | Required? | Default | Description                                                                                                   |
|--------------|------|-----------|---------|---------------------------------------------------------------------------------------------------------------|
| `SESSION_ID` | str  | Yes       |         | Advent of Code session ID cookie value. Can be found in the HTTP requests headers when using your web browser |

## Usage

Simply execute one of the scripts named after the corresponding year / day (e.g `python 2015_1.py`).