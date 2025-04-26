from gpiozero import DigitalInputDevice, DigitalOutputDevice
from time import sleep

flame_sensor = DigitalInputDevice(17) 
buzzer = DigitalOutputDevice(27)  
print("Flame sensor test started...")
while True:
    if flame_sensor.value == 0:
        print("🔥 Flame detected!")
        buzzer.on()  # Turn the buzzer on
    else:
        print("No flame.")
        buzzer.off()  # Turn the buzzer off
    sleep(0.5)
