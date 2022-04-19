import six
from src.writer import writer

def func():
	processor = writer()
	if isinstance(processor, writer):
		return True
	return False

def test_answer():
	assert func() == True