from MihoyoNetSniffer.packet import PipePacketStream
from pathlib import Path
from time import sleep, localtime, strftime


if __name__ == '__main__':
	output_path = Path(r'D:\yuanshen2\3.5.0\sniffer_log')
	output_name = '风花节'
	output_file_path = output_path / (output_name + strftime("-%Y-%m-%d-%H-%M-%S.dump", localtime()))
	a = PipePacketStream(dump_file=output_file_path)
	a.start()
	try:
		a.wait_for_connected()
		sleep(99999)
	except KeyboardInterrupt:
		a.stop()
