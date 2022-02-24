# Raspberry PI MidiController with E-ink display
## Purpose
Trying to create a solution here for controlling a MIDI device without a display using a Raspberry PI with an E-ink display
Using an e-ink display is more for fun here than to serve a purpose. Personally I like the technology a lot, so I wanted to play around with it. It's fascinating, that they keep the content even without power, see image below.

![alt text](https://github.com/stefan-karg/raspberryEinkMidiController/blob/main/midipi.jpg "Picture of unplugged Raspberry with eink display")


## Used hardware
* Raspberry PI Model 4
* Adafruit 2.13" Monochrome E-Ink Bonnet for Raspberry Pi - THINK INK (https://www.adafruit.com/product/4687)
* MIDIMATE eX (USB-to-MIDI)
## Required setup
* Install Raspbian
* For e-ink display:
  * Install circuitpython on Raspberry (https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
  * Install Adafruit EPaper library (https://learn.adafruit.com/2-13-in-e-ink-bonnet/usage)
  * Also install the 5x8 font binary as mentioned in the link
  * Install pillow library (also described in https://learn.adafruit.com/2-13-in-e-ink-bonnet/usage)
* For controlling MIDI:
  * Install python-rtmidi (https://pypi.org/project/python-rtmidi/)

