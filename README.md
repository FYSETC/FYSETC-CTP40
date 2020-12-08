# 4 INCH CTP LCD Drivers

4 INCH CTP LCD(CTP40) is an 800x480 pixel display for the Raspberry Pi, with optional capacitive touchscreen.

### Install

First clone this repo first, run 

```
git clone https://github.com/FYSETC/FYSETC-CTP40
```

There are two folder name `Pi3` and `Pi4`, If you are using  Raspberry Pi3 and older device, please follow the README file in `Pi3` folder. And if you are using Raspberry Pi4, then follow the README file in `Pi4` folder.

## Rotation

### Rotation on Pi 4

CTP40 is a portait display, so on first boot it will start in portrait mode with the USB ports at the top.

On Pi 4 we can take advantage of the rotation available in Display Configuration, and provide you with a command for setting both display and touch rotation together.

To rotate CTP40 on a Pi 4 use the `ctp40-rotate` command.

Landscape mode, HDMI/power ports on the bottom:

```
ctp40-rotate left
```

Landscape mode, HDMI/power ports on the top:

```
ctp40-rotate right
```

Portrait mode, USB ports on the top:

```
ctp40-rotate normal
```

Portrait mode, USB ports on the bottom:

```
ctp40-rotate inverted
```

If you're running this command over SSH you should prefix it with `DISPLAY=:0.0`

#### 180 Degree Rotation on Pi 3

Note: You *must* build the latest dtoverlay file to enable rotation support:

1. Go into `src` in `Pi3` folder
2. run `make` to build a new ctp40.dtbo with rotation support
3. copy the overlay with `sudo cp ctp40.dtbo /boot/overlays/`

To rotate your CTP40 you must edit /boot/config.txt and change the following lines:

1. Change `dtoverlay=ctp40` to `dtoverlay=ctp40:rotate`
2. Change `display_rotate=3` to `display_rotate=1`

This will rotate both the display and the touchscreen input to match.

If you're using a non-touchscreen CTP40 you need only change `display_rotate`.


