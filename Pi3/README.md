# 4.0 INCH CTP LCD Drivers for Raspberry Pi 3B+ or older

4.0 INCH CTP LCD(CTP40) is an 800x480 pixel display for the Raspberry Pi, with optional capacitive touchscreen.

These drivers are for Raspberry Pi models before the Pi 3B+.

## Installing / Uninstalling

1. Make sure you're running Raspbian Buster or Raspbian Stretch.

2. Update your Pi with `sudo apt update` and `sudo apt upgrade`.

3. Clone this GitHub repository to your Pi:

```
git clone https://github.com/FYSETC/FYSETC-CTP40
```

4. Then run the installer to install:

```
cd "Pi3"
sudo ./install.sh
```

## Rotation

To keep your touchscreen rotated with the display, you should rotate CTP40 using the `ctp40-rotate` command rather than "Screen Configuration."

This command will update your touch settings and screen configuration settings to match, and you can rotate between four modes: left, right, normal, inverted.

* `ctp40-rotate left` - landscape, power/HDMI on bottom
* `ctp40-rotate right` - landscape, power/HDMI on top
* `ctp40-rotate normal` - portrait, USB ports on top
* `ctp40-rotate inverted` - portrait, USB ports on bottom

This command changes the `display_rotate` parameter in `/boot/config.txt` and changes the touchscreen calibration dropped into `/etc/udev/rules.d/`.

## Touch rotation

If you're having trouble with your touch being 180 degrees rotated to your screen, or need to rotate the touch for other reasons you can use some additional arguments for the dtoverlay in config.txt, these are:

* `touchscreen-inverted-x`
* `touchscreen-inverted-y`
* `touchscreen-swapped-x-y`

For example, to rotate touch 180 degrees you want to invert both the x and y axis, by changing the `dtoverlay=ctp40` line in your `/boot/config.txt` to:

```
dtoverlay=ctp40,touchscreen-inverted-x,touchscreen-inverted-y
```

