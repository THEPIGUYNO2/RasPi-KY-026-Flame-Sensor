from gpiozero import DigitalInputDevice
from time import sleep

flame_sensor = DigitalInputDevice(17)  # GPIO17

print("Flame sensor test started...")
while True:
    if flame_sensor.value == 0:
        print("🔥 Flame detected!")
    else:
        print("No flame.")
    sleep(0.5)
