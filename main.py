# This is a sample Python script.

import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler(sys.stdout)
console_formatter = logging.Formatter("%(message)s")
console_handler.setFormatter(console_formatter)
console_handler.setLevel(logging.INFO)

logger.addHandler(console_handler)


def print_spring():
    logger.info("hello world!!!")
    string = ["My first program with python3 !", "Mw first program with docker !"]
    logger.info(string[0])
    logger.info(string[1])


def main():
    print_spring()


if __name__ == "__main__":
    main()
