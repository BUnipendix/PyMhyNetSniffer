from subprocess import Popen
PROTO_COMPILER = r"D:\yuanshen2\ps\protoc-3.20.1-win64\bin\protoc.exe"


def generate_one_proto(work_path, proto_paths, gen_proto_name=None, python_output_dir=None):
	def search(name):
		for i in search_path_list:
			file = i / name
			if file.is_file():
				return file

	def gen_core(cmd_set):
		new_cmd_set = set()

		for proto_name in cmd_set:
			# search
			if proto_name in fail_to_find:
				continue
			file = search(proto_name)
			if file is None:
				continue

			# parse
			get_top = False
			for line in file.open(encoding='utf-8'):
				if get_top is False:
					if line.startswith('message') or line.startswith('enum'):
						get_top = True
						floor_count = 0
						floor_start_flag = False
					elif line.startswith('import'):
						proto_name = eval(line[7:line.index(';', 7)])
						if proto_name not in all_loaded_set:
							new_cmd_set.add(proto_name)

				if get_top:
					output_file.write(line)
					floor_count += line.count('{')
					if floor_count > 0 and floor_start_flag is False:
						floor_start_flag = True
					floor_count += line.count('}')
					if floor_count <= 0 and floor_start_flag is True:
						get_top = False

		# get import
		if new_cmd_set:
			all_loaded_set.update(new_cmd_set)
			gen_core(new_cmd_set)

	from pathlib import Path
	cmd_set = {'HeaderPacket.proto'}
	fail_to_find = set()
	search_path_list = []

	if gen_proto_name is None:
		from MihoyoNetSniffer.constant import PROTO_NAME
		gen_proto_name = PROTO_NAME
	proto_output = Path(work_path) / (gen_proto_name + '.proto')

	if python_output_dir is None:
		from importlib.util import find_spec
		python_output_dir = Path(find_spec('MihoyoNetSniffer').origin).parent
	cmdid_path = python_output_dir / 'cmdid.csv'

	for i in proto_paths:
		search_path_list.append(Path(i))
	for line in open(cmdid_path, encoding='utf-8'):
		cmd_set.add(line[:line.index(',')] + '.proto')
	all_loaded_set = cmd_set.copy()

	with open(proto_output, 'w', encoding='utf-8') as output_file:
		output_file.write('syntax = "proto3";' '\n')
		gen_core(cmd_set)

	Popen((PROTO_COMPILER, '-I', work_path, '--python_out', python_output_dir, proto_output))
	return tuple(fail_to_find)


def json2csv(json_path, csv_path, is_reverse=False):
	import json
	with open(json_path, encoding='utf-8') as f:
		data = json.load(f)
	with open(csv_path, 'w', encoding='utf-8') as f:
		if is_reverse:
			for cmdid, field in data.items():
				f.write(f'{field},{cmdid}\n')
		else:
			for field, cmdid in data.items():
				f.write(f'{field},{cmdid}\n')


if __name__ == '__main__':
	from pathlib import Path
	work_path = Path(r'D:\yuanshen2\3.5.0\3.5_protos')
	cmdid_json = work_path / "packetIds.json"
	cmdid_csv = work_path / "cmdid.csv"
	proto_dirs = (
		'deobfuscated',
		'obfuscated'
	)
	new_proto_dir = []
	for i in proto_dirs:
		new_proto_dir.append(work_path / i)
	gen_proto_path = work_path
	json2csv(cmdid_json, cmdid_csv)
	print(generate_one_proto(work_path, new_proto_dir))
