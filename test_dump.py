from MihoyoNetSniffer import Sniffer
from time import sleep


if __name__ == '__main__':
	a = Sniffer(dump_path='test.bin', cache_packet=False)
	a.start()
	a.wait_for_connected()
	sleep(10)
	a.stop()
	a.load_from_file('test.bin')
	breakpoint()

