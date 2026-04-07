import digitalio
import rotaryio

class Encoder:
    def __init__(self, pin_a, pin_b, pin_sw):
        self._enc = rotaryio.IncrementalEncoder(pin_a, pin_b)
        self._last_pos = self._enc.position
        
        self._sw = digitalio.DigitalInOut(pin_sw)
        self._sw.direction = digitalio.Direction.INPUT
        self._sw.pull = digitalio.Pull.UP
        self._sw_last = self._sw.value

    def get_events(self):
        events = []
        pos = self._enc.position
        if pos != self._last_pos:
            direction = 'cw' if pos > self._last_pos else 'ccw'
            events.append(('encoder', direction))
            self._last_pos = pos

        sw = self._sw.value
        if not sw and self._sw_last:   # active low, falling edge = press
            events.append(('encoder', 'press'))
        elif sw and not self._sw_last:
            events.append(('encoder', 'release'))
        self._sw_last = sw
        return events