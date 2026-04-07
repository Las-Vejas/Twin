import busio
import json

class HABridge:
    """
    Sends simple JSON commands over UART to ESPHome on the ESP32.
    ESPHome on the other end exposes a UART component that parses
    incoming strings and maps them to HA actions.
    """
    def __init__(self, tx_pin, rx_pin, baudrate=115200):
        self.uart = busio.UART(tx_pin, rx_pin, baudrate=baudrate)

    def send(self, action: str, value=None):
        payload = {"action": action}
        if value is not None:
            payload["value"] = value
        msg = json.dumps(payload) + "\n"
        self.uart.write(msg.encode())

    # Convenience helpers — map these to your keys
    def toggle_light(self, entity="light.desk"):
        self.send("toggle", entity)

    def set_volume(self, delta: int):
        self.send("volume", delta)

    def media_play_pause(self):
        self.send("media_play_pause")

    def scene(self, name: str):
        self.send("scene", name)