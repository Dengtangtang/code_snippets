''' An example of using a simple logger.
'''

import logging
import logging.handlers
from logging import Formatter


def main():
    print(1/0)


if __name__ == '__main__':
    # Create a simple logger.
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.ERROR)
    log_filepath = 'logs/main.log'
    handler = logging.handlers.RotatingFileHandler(log_filepath,
                                                   maxBytes=1024000,
                                                   backupCount=2,
                                                   encoding='utf-8',
                                                   delay=False)
    log_format = '%(asctime)s >>> %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    handler.setFormatter(Formatter(log_format, date_format))
    logger.addHandler(handler)

    # Run main() with logging exceptions.
    try:
        main()
    except Exception:
        msg = 'Exception occured!'
        logger.exception(msg)
