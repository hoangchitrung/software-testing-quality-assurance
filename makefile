run:
	@pytest test_saucedemo.py --headed --slowmo 2000 --tracing on

trace:
	@playwright show-trace test-results/*/trace.zip