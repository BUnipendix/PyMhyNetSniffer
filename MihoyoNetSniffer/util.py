def get_main_dir():
	from os.path import dirname, abspath
	return dirname(abspath(__file__))


def check_filename(filename):
	import os
	new_filename, suffix = os.path.splitext(filename)
	count = 1
	while os.path.exists(new_filename + suffix):
		new_filename = f'{filename}({count})'
		count += 1
	return new_filename + suffix


