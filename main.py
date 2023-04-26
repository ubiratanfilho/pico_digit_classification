from time import sleep
import sys
sys.path.append('Pico_W_Stub/stubs/machine')
from machine import Pin

pin = Pin("LED", Pin.OUT)

while True:
    pin.toggle()
