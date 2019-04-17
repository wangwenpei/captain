"""
=============
基础类
=============
"""


# from .logger import logger

class Captain(object):
    def __init__(self, debug=False, dry_run=False, verbose=0):
        self.debug = debug
        self.dry_run = dry_run
        self.verbose_count = verbose
        # self.logger = logger
        pass
