import eink
import midi
display = eink.Eink()

display.init()
display.clearWhite()
#display.text()
display.update()

display.logText("[>] E-Ink init ok")
display.logText("[>] Midi init")

midiHandle = midi.UsbMidiController()
midiHandle.init(display)
display.logText("done")
