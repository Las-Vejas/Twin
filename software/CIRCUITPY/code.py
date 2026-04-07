import time
import board
from CIRCUITPY.config import *
from CIRCUITPY.matrix import KeyMatrix
from CIRCUITPY.encoder import Encoder
from CIRCUITPY.leds import LEDController
from CIRCUITPY.uart_ha import HABridge

# --- Key layout: (row, col) -> action name ---
KEYMAP = {
    (0, 0): "scene_morning",
    (0, 1): "scene_focus",
    (0, 2): "scene_evening",
    (1, 0): "media_play_pause",
    (1, 1): "toggle_light",
    (1, 2): "mute",
    (2, 0): "custom_1",
    (2, 1): "custom_2",
    (2, 2): "custom_3",
    # encoder push is handled separately
}

# Key index for underswitch LEDs (flatten row/col to index)
def key_to_led(row, col, num_cols=3):
    return row * num_cols + col

matrix  = KeyMatrix(ROW_PINS, COL_PINS)
encoder = Encoder(ENCODER_A, ENCODER_B, ENCODER_SW)
leds    = LEDController(UNDERGLOW_LED_PIN, UNDERSWITCH_LED_PIN,
                        NUM_UNDERGLOW, NUM_UNDERSWITCH)
ha      = HABridge(UART_TX, UART_RX, UART_BAUD)

# Startup: blue underglow, dim white underswitch
leds.set_underglow((0, 30, 80))
leds.set_all_underswitch((0, 20, 60, 0))

print("Macropad ready.")

while True:
    # --- Matrix events ---
    for (key, event) in matrix.get_events():
        led_idx = key_to_led(*key)
        if event == 'press':
            action = KEYMAP.get(key)
            leds.key_press_flash(led_idx)
            if action:
                ha.send(action)
                print(f"Key {key} -> {action}")
        elif event == 'release':
            leds.key_release(led_idx)

    # --- Encoder events ---
    for (_, event) in encoder.get_events():
        if event == 'cw':
            ha.send("volume", 5)
        elif event == 'ccw':
            ha.send("volume", -5)
        elif event == 'press':
            ha.send("media_play_pause")

    time.sleep(0.005)  # ~200Hz scan rate