import sys
from rtmidi.midiutil import open_midioutput, open_midiinput
from rtmidi.midiconstants import CONTROL_CHANGE

def open_midi_device():
    out_port = sys.argv[1] if len(sys.argv) > 1 else None
    in_port = sys.argv[2] if len(sys.argv) > 2 else None
    try:
        midiout, port_name = open_midioutput(out_port)
        midiin, _ = open_midiinput(in_port)
    except (EOFError, KeyboardInterrupt):
        sys.exit()
    return midiout, midiin, port_name

midiout, midiin, port_name = open_midi_device()

def channel(status, ch=None):
    return (status & 0xF0) | ((ch if ch else 0) & 0xF)

def send_cc(cc, val, ch=None):
    message = [channel(CONTROL_CHANGE, ch), cc, val]
    # print('sending message {}'.format(message))
    midiout.send_message(message)
