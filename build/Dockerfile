FROM ubuntu:latest

WORKDIR ./app

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip \
 	python3-pytest \
  	python3-pygame \
	git

RUN mkdir -p /snake/dist/log

RUN git clone https://github.com/kkanie/snakegame-gui.git
