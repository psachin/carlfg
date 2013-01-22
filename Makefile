# Makefile for carlfg

all: 
	@echo "doing nothing"

install:
	@echo "building distrubution packages....."
	sudo python setup.py sdist
	@echo "installing packages....."
	sudo python setup.py install

clean:
	@echo "cleaning up ....."
	sudo rm -rvf carlfg.egg-info dist build

