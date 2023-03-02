from .sniffer import Sniffer
import logging

# Log Inital
logger = logging.getLogger('MihoyoNetSniffer')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)-4s: %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler('MihoyoNetSniffer.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)-4s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

