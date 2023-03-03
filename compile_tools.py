import os
from subprocess import Popen
PROTO_COMPILER = r"D:\yuanshen2\ps\protoc-3.20.1-win64\bin\protoc.exe"


def generate_one_proto(input_path, output_path):
	from pathlib import Path
	with open(output_path, 'w', encoding='utf-8') as output_file:
		output_file.write('syntax = "proto3";' '\n')
		input_path = Path(input_path)

		for i in input_path.iterdir():
			if not i.name.endswith('.proto') or i.is_dir():
				continue

			get_top = False
			for line in i.open(encoding='utf-8'):

				if get_top is False and line.startswith('message') or line.startswith('enum'):
					get_top = True
					floor_count = 0
					floor_start_flag = False

				if get_top:
					output_file.write(line)
					floor_count += line.count('{')
					if floor_count > 0 and floor_start_flag is False:
						floor_start_flag = True
					floor_count += line.count('}')
					if floor_count <= 0 and floor_start_flag is True:
						get_top = False

	output_dir = os.path.dirname(output_path)
	data = (PROTO_COMPILER, '--proto_path', output_dir, '--python_out', output_dir, output_path)
	Popen(data)


def json2csv(json_path, csv_path):
	import json
	with open(json_path, encoding='utf-8') as f:
		data = json.load(f)
	with open(csv_path, 'w', encoding='utf-8') as f:
		for cmdid, field in data.items():
			f.write(f'{field},{cmdid}\n')


if __name__ == '__main__':
	json2csv(r"D:\yuanshen2\3.5.0\deof_proto\packetIds.json", r"D:\yuanshen2\3.5.0\deof_proto\cmdid.csv")
	generate_one_proto(r'D:\yuanshen2\3.5.0\deof_proto\protos', r'D:\yuanshen2\3.5.0\deof_proto\genshin_proto.proto')
