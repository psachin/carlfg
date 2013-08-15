# Makefile for carlfg

all: 
	@echo "doing nothing"

build:
	@echo "building distrubution packages....."
	sudo python setup.py sdist

install:
	@echo "installing packages....."
	sudo python setup.py install

clean:
	@echo "cleaning up ....."
	sudo rm -rvf carlfg.egg-info dist build

