from __future__ import absolute_import, division, print_function

import logging
from pathlib import Path
import os

def logger() -> logging.Logger:
    """Create logging infrastructure
    
    Returns:
        [logging.Logger] -- logger object used for logging infrastructure 
    """

    logger = logging.getLogger('flow2vec')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

    return logger
    
def make_log_dir(log_dir: str, logger: logging.Logger):
    """Create tensorboard log directory
    
    Arguments:
        log_dir {str} -- directory on file system to save Tensorboard Log File(s)
    """

    log_dir = Path(log_dir)

    if log_dir.exists():
        logger.info(f'Tensoboard log directory {log_dir} already exists!')
    else:
        os.makedirs(log_dir)
        logger.info(f'Tensorboard Log Directory {log_dir} created!')
