import board

# Key Matrix - match your schematic labels
ROW_PINS = [board.GPIO9, board.GPIO10, board.GPIO11]   # r1, r2, r3
COL_PINS = [board.GPIO15, board.GPIO14, board.GPIO13]  # c1, c2, c3 (+ c4 if needed)

# Rotary Encoder (top-right key position)
ENCODER_A = board.GPIO6   # 1A
ENCODER_B = board.GPIO7   # 1B
ENCODER_SW = board.GPIO8  # underswitch for encoder

# LEDs
UNDERSWITCH_LED_PIN = board.GPIO28  # underswitch (11x SK6812MINI)
UNDERGLOW_LED_PIN   = board.GPIO16  # backlight (14x WS2812B)

NUM_UNDERSWITCH = 11
NUM_UNDERGLOW   = 14

# UART to ESP32
UART_TX = board.GPIO0  # ESP-TX on schematic
UART_RX = board.GPIO1  # ESP-RX on schematic
UART_BAUD = 115200