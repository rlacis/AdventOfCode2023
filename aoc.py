import logging
import requests
import time
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('AoC')


def read_input(filename: str) -> str:
    with open(filename) as f:
        contents = f.read()
        return contents


def write_input_file(aoc_day: int, contents: str, **kwargs) -> bool:
    filename_suffix = kwargs.get('filename_suffix', '')
    with open(f'Input/day_{aoc_day:02}{filename_suffix}.txt', 'w') as f:
        f.write(contents)
    return True


def split_contents(contents: str) -> list:
    """
    Splits a string from a text file delimited with new lines.
    :param contents: Input string read from the input file
    :return: List of strings split by lines
    """
    return contents.strip().split('\n')


def get_puzzle_input(aoc_day: int, aoc_year: int) -> str:
    """
    Get the session ID from the network inspector in a browser.
    :param aoc_day: Day number, 1 to 25
    :param aoc_year: 2023
    :return: raw text of the puzzle input
    """
    cookies = {'session': '53616c7465645f5f01f0cecd723be2048d75a7465404b0290873d7797525bf4dbbb3992fbad340b34ee7bfa40caac40c0767aff59c5d7c1373dc2ec8939fe601'}
    r = requests.get(f'https://adventofcode.com/{aoc_year}/day/{aoc_day}/input', cookies=cookies)
    return r.text


def timer_func():
    # This decorator function shows the execution time of the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        logger.info(f'Function {func.__name__!r} executed in {(t2 - t1):.2f}s')
        return result
    return wrap_func
