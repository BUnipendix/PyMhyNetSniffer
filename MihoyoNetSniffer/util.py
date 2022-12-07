import os
from subprocess import Popen, DEVNULL


PROTO_COMPILER = r"D:\yuanshen2\ps\protoc-3.20.1-win64\bin\protoc.exe"


def generate_code(input_path, output_path):
	input_path = modify_path(input_path)
	output_path = modify_path(output_path)
	tasks = []
	for i in os.listdir(input_path):
		if not i.endswith('.proto'):
			continue
		tasks.append(
			Popen((
				PROTO_COMPILER,
				'--proto_path=' + input_path,
				'--python_out', output_path, i),
				stdin=DEVNULL,  stdout=DEVNULL)
		)
	for i in tasks:
		i.wait()


def remove_extra_info(input_path, output_path):
	input_path = modify_path(input_path)
	output_path = modify_path(output_path)
	for i in os.listdir(input_path):
		if not i.endswith('.proto'):
			continue
		name = input_path + i
		tmp_name = output_path + i
		with open(tmp_name, 'w', encoding='utf-8') as f:
			get_top = False
			for line in open(name, 'r', encoding='utf-8'):
				if get_top is False and line.startswith('message'):
					get_top = True
				if (not line.startswith('//')) and (not line.startswith('option') and (len(line) > 1 or get_top)):
					f.write(line)


def modify_path(path):
	if path:
		path = path.replace('\\', '/')
		if path[-1] != '/':
			path = path + '/'
	return path


def varint(data):
	num = 0
	count = 0
	for i in data:
		num += i << count
		if not (num >> 7):
			break
		count += 7
	return num


remove_extra_info(r'D:\Android\Sorapointa-Protos\proto', r'D:\Android\Sorapointa-Protos\sproto')
generate_code(r'D:\Android\Sorapointa-Protos\sproto', r'D:\Android\PyMhyNetSniffer\MihoyoNetSniffer\generated_python_code')
