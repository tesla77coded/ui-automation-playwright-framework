from loguru import logger
import sys


def get_logger():
    logger.remove()
    logger.add(sys.stdout, level="INFO")
    logger.add("reports/test.log", rotation="1 MB")
    return logger
