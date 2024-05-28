
from machine import ADC, Pin
import time


from adc_sub import ADC_substitute


pin_battery = 32                      





# Battery
battery = ADC_substitute(pin_battery)  # The battery object

ip1 = 1903
#ip1 = 3653
ip2 = 2756
#ip2 = 4095
bp1 = 0                                # Battery percentage when fully discharged
bp2 = 100                              # Battery percentage when fully charged
alpha = (bp2 - bp1) / (ip2 - ip1)      # alpha is the slope in the first degree equation bp = alpha * input + beta
print(f'Alpha: {alpha}')

beta = bp1 - alpha * ip1               # beta is the crossing point on the y axis
print(f'Beta: {beta}')



def get_battery_percentage():          # The battery voltage percentage
    ip = battery.read_adc()            # Either use this or the one below. Remove if not used
    print(f'IP: {ip}')

    
    bp = alpha * ip + beta             # Calculate the battery percentage based on the measured input value
    bp = int(bp)
    print(f'BP1: {bp}')# Take the interger value
    
   
    if bp < 0:                         
        bp = 0
    elif bp > 100:
        bp = 100
    
    return bp


while True:
    # Measure the battery percentage
    bat_pct = get_battery_percentage()
    
    print(f'Bat%: {bat_pct}')
    time.sleep(0.5)
    

