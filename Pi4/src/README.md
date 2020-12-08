# 4 INCH CTP LCD Drivers

## ctp40-init.c

Source for the ctp40-init binary.

It's designed to be statically linked against bcm2835 and runs all of the init routine required for CTP40

## ctp40.dts

Source for hyperpixel4.dtbo device-tree overlay.

This overlay sets up:

* GPIO backlight (on/off) functionality
* Goodix multitouch digitiser
