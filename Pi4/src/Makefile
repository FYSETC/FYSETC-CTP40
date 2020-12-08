build:
	dtc -I dts -O dtb -Wno-unit_address_vs_reg -o ctp40.dtbo ctp40.dts

install:
	cp ctp40.dtbo /boot/overlays/

test:
	dtoverlay ctp40.dtbo
