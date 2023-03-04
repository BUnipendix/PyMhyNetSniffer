from MihoyoNetSniffer.sniffer import Sniffer
from MihoyoNetSniffer import logger
from logging import INFO, DEBUG
logger.setLevel(INFO)


if __name__ == '__main__':
	a = Sniffer()
	from MihoyoNetSniffer.constant import COMMON_UNIMPORTENT_PACKETS, PLAYER_RELATED_PACKETS, AI_RELATED_UNIMPORTANT_PACKETS
	a.add_to_list(*COMMON_UNIMPORTENT_PACKETS,
				  *PLAYER_RELATED_PACKETS,
				  *AI_RELATED_UNIMPORTANT_PACKETS,
				  'SceneTeamUpdateNotify')
	a.load_from_file(r"D:\yuanshen2\3.5.0\sniffer_log\GenshinKCP-2023-03-02-20-59-46.dump")
	from MihoyoNetSniffer.util import generate_printed_packet
	with open(r"D:\yuanshen2\3.5.0\sniffer_log\test.log", 'w', encoding='utf-8') as f:
		for i in a.packets.values():
			print(generate_printed_packet(i), file=f)
