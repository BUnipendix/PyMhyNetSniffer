from MihoyoNetSniffer.sniffer import Sniffer
from MihoyoNetSniffer import logger
from logging import INFO, DEBUG
logger.setLevel(INFO)


if __name__ == '__main__':
	a = Sniffer()
	from MihoyoNetSniffer.util import COMMON_UNIMPORTENT_PACKETS
	a.add_to_list(*COMMON_UNIMPORTENT_PACKETS, 'AbilityInvocationsNotify')
	a.load_from_file(r"D:\yuanshen2\3.5.0\sniffer_log\GenshinKCP-2023-03-02-20-59-46.dump")
	breakpoint()
