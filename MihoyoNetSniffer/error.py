class LogException(Exception):
	def __init__(self, *value):
		from sys import _getframe
		self.value = value
		logger = _getframe(1).f_globals.get('logger', None)
		if logger:
			logger.error(self.__str__())


class FileEndError(LogException):
	def __str__(self):
		req_size, real_size, file_obj = self.value
		if file_obj:
			name = file_obj.__dict__.get('name', '')
			size = file_obj.tell()
			read_point = size - real_size
			result = '文件%s在%s的位置' % (name, read_point)
		else:
			result = '流被'
		return result + '请求读取%s字节的数据结果读取了%s个字节' % (req_size, real_size)


class PipeError(LogException):
	def __str__(self):
		return '读取错误：错误码：%s， 数据：%s' % self.value