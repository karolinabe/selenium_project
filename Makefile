setup:
	pip install selenium
	wget https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-linux64.tar.gz
	tar -xvf geckodriver-v0.21.0-linux64.tar.gz
	mkdir /home/travis/virtualenv/python2.7.12/bin
	mv geckodriver /usr/local/bin
test:
	python yahoo_test1.py
