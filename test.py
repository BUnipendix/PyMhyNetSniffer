from MihoyoNetSniffer.sniffer import Sniffer
from MihoyoNetSniffer.packet import GameNetwork
from base64 import b64encode

def test(uid, packet):
	try:
		for i in packet.content.parent_quest_list:
			if i.Unk2700_KHDDIJNOICK:
				print(f'{i.parent_quest_id}: {i.Unk2700_KHDDIJNOICK}')
	except Exception:
		pass




#a = GameNetwork('genshin_packet_pipe')
#a.start()
from time import sleep
# sleep(10)
# a.stop()
a = Sniffer(r"D:\yuanshen2\tmp\3.1.0\Sorapointa-Protos-3.1.0\cmdid.csv")
print('完成')
a.add_handle('FinishedParentQuestNotify', test)
a.add_handle('FinishedParentQuestUpdateNotify', test)
a.start()
try:
	sleep(3000)
except KeyboardInterrupt:
	pass
finally:
	a.stop()
	breakpoint()
