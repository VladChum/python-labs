#!/usr/bin/env python
# This is a sample Python script.
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout,
                    format='%(message)s')


def main():
    logger.info("hello world!!!")
    for x in ["My first program with python3 !", "Mw first program with docker !"]:
        logger.info(x)


if __name__ == "__main__":
    main()
