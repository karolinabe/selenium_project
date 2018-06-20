setup:
	pip install selenium
	wget https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-linux64.tar.gz
	tar -xvf geckodriver-v0.21.0-linux64.tar.gz
	
test:
	python yahoo_test1.py
