import logging
import os

import gaylogger as glogging
from gaylogger import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_basic_functionality():
    print("starting to log")

    for i in range(0, 9):
        logger = glogging.getLogger(f"main{i}", logging.DEBUG, split="=")
        for j in range(2):
            logger.warning("im about to reveal my gender")
        logger.info("hi im gay")
        logger.error("gay not found")
        logger.debug("tried to assign <gay> as gender but could not accomplish")
        logger.debug("gender must be one of ['male','female']")
        logger.critical("your gender is not accepted!")


def test_env_log_level():
    print(f"log level is {os.getenv('GAY_LEVEL')}")
    logger = glogging.getLogger("env", split="=")
    for j in range(2):
        logger.warning("im about to reveal my gender")
    logger.info("hi im gay")
    logger.error("gay not found")
    logger.debug("tried to assign <gay> as gender but could not accomplish")
    logger.debug("gender must be one of ['male','female']")
    logger.critical("your gender is not accepted!")
