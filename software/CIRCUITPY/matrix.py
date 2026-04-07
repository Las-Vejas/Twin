import digitalio
import time

class KeyMatrix:
    def __init__(self, row_pins, col_pins):
        self.rows = []
        self.cols = []
        self._state = {}

        for pin in row_pins:
            r = digitalio.DigitalInOut(pin)
            r.direction = digitalio.Direction.OUTPUT
            r.value = False
            self.rows.append(r)

        for pin in col_pins:
            c = digitalio.DigitalInOut(pin)
            c.direction = digitalio.Direction.INPUT
            c.pull = digitalio.Pull.DOWN
            self.cols.append(c)

    def scan(self):
        """Returns dict of (row, col) -> bool pressed state."""
        current = {}
        for r_idx, row in enumerate(self.rows):
            row.value = True
            time.sleep(0.001)  # settling time
            for c_idx, col in enumerate(self.cols):
                key = (r_idx, c_idx)
                current[key] = col.value
            row.value = False
        return current

    def get_events(self):
        """Returns list of (key_id, 'press'|'release') events."""
        current = self.scan()
        events = []
        for key, pressed in current.items():
            was_pressed = self._state.get(key, False)
            if pressed and not was_pressed:
                events.append((key, 'press'))
            elif not pressed and was_pressed:
                events.append((key, 'release'))
        self._state = current
        return events