# 4 INCH CTP LCD Drivers for Raspberry Pi 4

4 INCH CTP LCD(CTP40) is an 800x480 pixel display for the Raspberry Pi, with optional capacitive touchscreen.

These drivers are for the Raspberry Pi 4 specifically, and include new tools to take advantage of the "Screen Configuration" (xrandr) support that Pi 4's 3D accelerated desktop enables.

## Installing / Uninstalling

First, clone this GitHub repository branch to your Pi:

```
git clone https://github.com/FYSETC/FYSETC-CTP40
```

Then run the installer to install:

```
cd FYSETC-CTP40/Pi4
sudo ./install.sh
```

*Note: this script is base on the script from hyperpixel4.*

## Rotation

To keep your touchscreen rotated with the display, you should rotate CTP40 using the `ctp40-rotate` command rather than "Screen Configuration."

This command will update your touch settings and screen configuration settings to match, and you can rotate between four modes: left, right, normal, inverted.

* left - landscape, power/HDMI on bottom
* right - landscape, power/HDMI on top
* normal - portrait, USB ports on top
* inverted - portrait, USB ports on bottom

If you want to change the position of your CTP40 in a multi-display setup, you can use "Screen Configuration" as normal.

Note: This is only works in Raspberry desktop system at the moment. And make sure you already set the the XAUTHORITY environment variable, for example you can 

```
export XAUTHORITY=/home/pi/.Xauthority
```

## Touch rotation

If you're having trouble with your touch being 180 degrees rotated to your screen, or need to rotate the touch for other reasons you can use some additional arguments for the dtoverlay in config.txt, these are:

* `touchscreen-inverted-x`
* `touchscreen-inverted-y`
* `touchscreen-swapped-x-y`

For example, to rotate touch 180 degrees you want to invert both the x and y axis, by changing the `dtoverlay=ctp40` line in your `/boot/config.txt` to:

```
dtoverlay=ctp40,touchscreen-inverted-x,touchscreen-inverted-y
```
