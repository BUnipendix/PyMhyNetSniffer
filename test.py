from MihoyoNetSniffer.sniffer import Sniffer
from MihoyoNetSniffer.packet import GameNetwork
from base64 import b64encode

def test(uid, packet):
	try:
		for i in packet.content.parent_quest_list:
			if i.video_key:
				print(f'{i.parent_quest_id}: {i.video_key}')
	except Exception:
		pass




#a = GameNetwork('genshin_packet_pipe')
#a.start()
from time import sleep
# sleep(10)
# a.stop()
a = Sniffer()
print('完成')
a.add_handle('FinishedParentQuestNotify', test)
a.add_handle('FinishedParentQuestUpdateNotify', test)
a.start()
try:
	a.process_loop.join()
except KeyboardInterrupt:
	pass
finally:
	a.stop()
	breakpoint()
