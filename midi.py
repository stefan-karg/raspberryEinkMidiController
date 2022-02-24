import rtmidi
import time

class UsbMidiController:
	MidiChannel = 1
	
	midiConnection = None
	display = None
	
	def init(self, displayIn):
		self.display = displayIn
		midiout = rtmidi.MidiOut()
		
		available_ports = midiout.get_ports()
		logStr = "[i] MIDI Ports = " + str(len(available_ports))
		self.display.logText(logStr)
		self.display.update()

		if available_ports:
			print("Port found")
			midiout.open_port(2)


		with midiout:
			note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
			note_off = [0x80, 60, 0]
			midiout.send_message(note_on)
			time.sleep(0.5)
			midiout.send_message(note_off)
			time.sleep(0.1)
			midiout.send_message(note_on)
			time.sleep(0.5)
			midiout.send_message(note_off)
			time.sleep(0.1)
		del midiout
		
		
