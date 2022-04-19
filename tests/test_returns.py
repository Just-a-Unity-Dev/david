from src.writer import writer

def func():
	processor = writer()
	return processor.write(0, "test")

def test_answer():
	if func() == "write 0 bank1 test":
		if len(func()) == 18:
			assert True
			return
	assert False