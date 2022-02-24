import rtmidi
import time

class UsbMidiController:
	MidiChannel = 1
	
	midiConnection = None
	
	def init(self):
		midiout = rtmidi.MidiOut()
		
		available_ports = midiout.get_ports()
		print("Ports:", available_ports)

		if available_ports:
			print("Port found")
			midiout.open_port(2)
		else:
			print("Virtual port")
			midiout.open_virtual_port("My virtual output")

		with midiout:
			note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
			note_off = [0x80, 60, 0]
			midiout.send_message(note_on)
			time.sleep(0.5)
			midiout.send_message(note_off)
			time.sleep(0.1)
		del midiout
		
		
