import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger('CryptoDevToolkit')
    logger.setLevel(logging.DEBUG)
    
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger initialized with rotation settings.')
    log.debug('This is a debug message.')
    log.warning('This is a warning message.')
    log.error('This is an error message.')
    log.critical('This is a critical message.')