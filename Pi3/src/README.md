# 4.0 INCH CTP LCD Drivers

## ctp40-init.c

Source for the ctp40-init binary.

It's designed to be statically linked against bcm2835 and runs all of the init routine required for ctp40

## ctp40.dts

Source for ctp40.dtbo device-tree overlay.

This overlay sets up:

* GPIO backlight (on/off) functionality
* Goodix multitouch digitiser
