from MihoyoNetSniffer.sniffer import Sniffer
from MihoyoNetSniffer.constant import COMMON_UNIMPORTENT_PACKETS, AI_RELATED_UNIMPORTANT_PACKETS, PLAYER_RELATED_PACKETS
from time import sleep
from traceback import print_exc


def test(_, packet):
	try:
		for i in packet.parent_quest_list:
			if i.video_key:
				print(f'{i.parent_quest_id}: {i.video_key}')
	except Exception as e:
		print_exc()
		print(e)
		pass


def test2(_, packet):
	print(f'{packet.parent_quest_id}: {packet.video_key}')


a = Sniffer(dump_path=r'D:\yuanshen2\3.5.0\sniffer_log', cache_packet=False, enable_data_output=True)
print('Initial success')
a.add_to_list(*COMMON_UNIMPORTENT_PACKETS)
a.add_to_list(*PLAYER_RELATED_PACKETS)
a.add_to_list(*AI_RELATED_UNIMPORTANT_PACKETS)
a.add_handle('FinishedParentQuestNotify', test)
a.add_handle('FinishedParentQuestUpdateNotify', test)
a.add_handle('GetParentQuestVideoKeyRsp', test2)
a.start()
try:
	sleep(9999)
except KeyboardInterrupt:
	pass
finally:
	print('Stopping Sniffer...')
	a.stop()
	print('Stop success')
	breakpoint()
