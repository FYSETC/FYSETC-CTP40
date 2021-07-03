import pigpio
gpio = pigpio.pi()
gpio.set_PWM_dutycycle(19, 128)  #0-255, so 128 is 1/2 duty cycle
