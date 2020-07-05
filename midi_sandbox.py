import time
import logging

from numpy.random import randint
from rtmidi.midiconstants import CONTROL_CHANGE, NRPN_LSB, NRPN_MSB


from funcs import open_midi_device, send_cc

log = logging.getLogger('digi-lfo')
logging.basicConfig(level=logging.DEBUG)

midiout, midiin, port_name = open_midi_device()
midiin.ignore_types()

def midiin_callback(event, data=None):
    msg, dt = event
    print('@@%0.6f %r' % (dt, msg))


try:
    # midiin.set_callback(midiin_callback)
    while True:
        # message = [CONTROL_CHANGE, FILTER_CHANNEL, np.random.randint(0, 127)]
        # midiout.send_message(message)
        # log.debug('sending message {}'.format(message))
        # send_cc(NRPN_MSB, randint(1, 4))
        send_cc(FILTER_CHANNEL, randint(0, 127), ch=randint(0, 7))
        time.sleep(0.1)
except KeyboardInterrupt:
    print('Keyboard interrupt, exiting')
finally:
    print('Exit')
    midiin.close_port()
    midiout.close_port()
    del midiin
    del midiout
