import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
def add(a, b):
    logger.debug(f"Adding {a} and {b}")
    return a+b

