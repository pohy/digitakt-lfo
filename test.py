import sys
from time import sleep

try:
    while True:
        print('lloop')
        sleep(1)
except KeyboardInterrupt:
    print('exiting')
finally:
    sys.exit()