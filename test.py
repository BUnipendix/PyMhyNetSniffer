from MihoyoNetSniffer.sniffer import Sniffer
from time import sleep


def test(_, packet):
	try:
		for i in packet.content.parent_quest_list:
			if i.video_key:
				print(f'{i.parent_quest_id}: {i.video_key}')
	except Exception:
		pass


a = Sniffer(cache_packet=False)
print('Initial success')
a.add_handle('FinishedParentQuestNotify', test)
a.add_handle('FinishedParentQuestUpdateNotify', test)
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
