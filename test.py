from MihoyoNetSniffer.sniffer import Sniffer
from MihoyoNetSniffer.packet import GameNetwork

def test(uid, packet):
	breakpoint()




#a = GameNetwork('genshin_packet_pipe')
#a.start()
from time import sleep
# sleep(10)
# a.stop()
a = Sniffer(r"D:\yuanshen2\3.0\Sorapointa-Protos\cmdid.csv")
print('完成')
# a.add_handle('FinishedParentQuestNotify', test)
a.start()
try:
	sleep(300)
except KeyboardInterrupt:
	a.stop()
finally:
	breakpoint()
