build:
	dtc -I dts -O dtb -o ctp40.dtbo ctp40.dts

install:
	cp ctp40.dtbo /boot/overlays/

test:
	dtoverlay ctp40.dtbo

init:
	gcc -o ctp40-init -static ctp40-init.c -lbcm2835
