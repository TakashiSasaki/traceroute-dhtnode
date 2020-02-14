#!/usr/bin/python3
import logging
class HelloLogger():
    def __init__(self, logger=None):
        if logger is None:
            logger = logging.getLogger(__name__)
        self.logger = logger

    def hello(self):
        self.logger.debug("hello debug")
        self.logger.info("hello info")
        self.logger.info(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    helloLogger = HelloLogger()
    helloLogger.hello()
