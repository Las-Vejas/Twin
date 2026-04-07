import neopixel

class LEDController:
    def __init__(self, underglow_pin, underswitch_pin, num_underglow, num_underswitch):
        self.underglow = neopixel.NeoPixel(
            underglow_pin, num_underglow,
            brightness=0.3, auto_write=False, pixel_order=neopixel.GRB
        )
        self.underswitch = neopixel.NeoPixel(
            underswitch_pin, num_underswitch,
            brightness=0.5, auto_write=False, pixel_order=neopixel.GRBW  # SK6812 has white channel
        )

    def set_underglow(self, color):
        """Set all underglow LEDs to a color (r, g, b)."""
        self.underglow.fill(color)
        self.underglow.show()

    def set_underswitch(self, index, color):
        """Set a single underswitch LED. color = (r, g, b, w)."""
        self.underswitch[index] = color
        self.underswitch.show()

    def key_press_flash(self, key_index):
        """Flash the LED under a pressed key white briefly."""
        self.underswitch[key_index] = (0, 0, 0, 255)  # pure white via W channel
        self.underswitch.show()

    def key_release(self, key_index, base_color=(0, 64, 128, 0)):
        self.underswitch[key_index] = base_color
        self.underswitch.show()

    def set_all_underswitch(self, color):
        self.underswitch.fill(color)
        self.underswitch.show()