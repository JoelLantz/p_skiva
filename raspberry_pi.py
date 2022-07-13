from machine import Pin, PWM
import utime

servo = PWM(Pin(0))
led = Pin(25, Pin.OUT)

servo.freq(50)
led.toggle()

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

#0 degrees = 1000, 180 degrees = 7500. Increments of 271 = 180/24
angle = 1000

while True:
    # Move servo to zero degrees (2 per cent duty cycle)
    servo.duty_u16(angle)
    angle = angle + 271
    
    if angle > 7505:
        led.toggle()
        break
    else:
        continue
    
    utime.sleep(1800)