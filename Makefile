export PATH := $(shell pwd)/bin:$(PATH)

setup:
	pip install selenium
	wget https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-linux64.tar.gz
	mkdir -p ./bin
	tar -xvf geckodriver-v0.21.0-linux64.tar.gz -C bin
	
test:
	python yahoo_test1.py
