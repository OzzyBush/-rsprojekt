from machine import Pin
import time

# Definer pins for rotary encoder signaler
pin_a = Pin(14, Pin.IN)
pin_b = Pin(12, Pin.IN)

# Initialiser tælleren
counter = 0

# Variabler til at holde styr på tidligere og nuværende state
last_state_a = pin_a.value()

def rotary_handler(pin):
    global counter, last_state_a
    current_state_a = pin_a.value()
    current_state_b = pin_b.value()
    
    if current_state_a != last_state_a:
        if current_state_a == 1:
            if current_state_b == 0:
                counter += 1
            else:
                counter -= 1
        
        # Print counter værdi
#         print("Counter:", counter)
        
        # Tjek værdien af counter og print passende sektion
        if counter <= 15:
            print("Borde 1-10")
        else:
            print("Borde 11-20")
        
    last_state_a = current_state_a

# Opsæt interrupts for rotary encoder
pin_a.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=rotary_handler)

try:
    while True:
        # En lille pause for at undgå for meget CPU brug
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program stoppet af bruger")

