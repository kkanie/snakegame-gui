FROM ubuntu:latest

WORKDIR ./app

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip \
	git

RUN git clone https://github.com/kkanie/snakegame-gui.git

WORKDIR ./snakegame-gui

RUN pip install pygame \
	pytest
