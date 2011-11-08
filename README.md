FLOSS Python driver for UNI-T UT2025B scopes
============================================

[![Flattr Button](http://api.flattr.com/button/button-static-50x60.png "Flattr This!")](https://flattr.com/thing/432544/FLOSS-Python-driver-for-UNI-T-UT2025B-scopes "Flattr")

Usage
-----

Connect the scope via USB, and issue the `python getshot.py >foo.bin` command.
In case of an "Image transfer error, try again" message, just keep trying,
after 10 or so attempts, it starts to work, and continues to do so, until the
scope is connected to the PC.

If the exit value is 0, and no output is printed on stderr, the binary
screenshot is ready in the `foo.bin` file. It can be converted to PNG by
issuing the following command, which currently uses the color scheme of
monochrome devices.

	python pd2png.py foo.bin foo.png

License
-------

The whole project is licensed under MIT license.

Dependencies
------------

 - Python 2.x (tested with 2.7)
 - PyUSB 1.0 (http://sourceforge.net/projects/pyusb/)
