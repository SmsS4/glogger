import gaylogger as logging
from gaylogger import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_basic_functionality():
    print("starting to log")

    for i in range(0, 9):
        logger = logging.getLogger(f"main{i}", logging.DEBUG, split="=")
        for j in range(20):
            logger.warning("im about to reveal my gender")
        logger.info("hi im gay")
        logger.error("gay not found")
        logger.debug("tried to assign <gay> as gender but could not accomplish")
        logger.debug("gender must be one of ['male','female']")
        logger.critical("your gender is not accepted!")
