"""
=============
基础类
=============
"""

from .logger import logger, logging


class Captain(object):
    def __init__(self, debug=False, dry_run=False, verbose=0):
        self.debug = debug
        self.dry_run = dry_run
        self.verbose_count = verbose
        self.logger = logger
        self.logger_level = logging.CRITICAL

        if verbose == 1:
            self.logger_level = logging.ERROR
        elif verbose == 2:
            self.logger_level = logging.WARNING
        elif verbose == 3:
            self.logger_level = logging.INFO
        else:
            self.logger_level = logging.DEBUG
            pass

        if self.debug:
            self.logger_level = logging.DEBUG

        self.logger.setLevel(self.logger_level)
        pass
