#This code is based on code by John Gallaugher's original code: 
# https://github.com/gallaugher/baby-groot

#His notes:
# For this code to work, your CPX must have four files on it, each named:
# I_am_groot_1.wav, I_am_groot_2.wav, I_am_groot_3.wav, and I_am_groot_4.wav
# The code cycles through these four sounds, each time a capacitive touch on
# CPX is registered (e.g. when you touch Groot's leaves). 

#my notes
# I have added an LED to the board that lights up



from adafruit_circuitplayground.express import cpx
import time
import board
import neopixel
import adafruit_lis3dh

# CUSTOMIZE YOUR COLOR HERE:
COLOR = (255, 0, 0)  # jedi
OFF = (0,0,0)


NUM_PIXELS = 30                        # NeoPixel strip length (in pixels)
NEOPIXEL_PIN = board.A2 # Pin where NeoPixels are connected
STRIP = neopixel.NeoPixel(NEOPIXEL_PIN, NUM_PIXELS, brightness=1, auto_write=False)
STRIP.fill(0)                          # NeoPixels off ASAP on startup
STRIP.show()

REALITY_STONE = (90, 0, 0)
MIND_STONE = (45, 45, 0)
TIME_STONE = (0, 90, 0)
SPACE_STONE = (0, 0, 90)
POWER_STONE = (45, 0, 45)


cpx.play_file("I_am_groot_1.wav")
soundNumber = 1
cpx.adjust_touch_threshold(200)
 
while True:
    if cpx.button_a:
        time.sleep(10)
        cpx.play_file("I_am_groot_1.wav")    
        cpx.pixels.fill(TIME_STONE)
        STRIP.fill(TIME_STONE)
        STRIP.show()
        time.sleep(1)
        cpx.pixels.fill(REALITY_STONE)
        STRIP.fill(REALITY_STONE)
        STRIP.show()        
        time.sleep(1)
        cpx.pixels.fill(MIND_STONE)
        STRIP.fill(MIND_STONE)
        STRIP.show()   
        time.sleep(1)
        cpx.pixels.fill(SPACE_STONE)
        STRIP.fill(SPACE_STONE)
        STRIP.show()    
        time.sleep(1)
        cpx.pixels.fill(POWER_STONE)
        STRIP.fill(POWER_STONE)
        STRIP.show()        
    if cpx.button_b:        
        cpx.pixels.fill(OFF)
        STRIP.fill(OFF)      # Set to idle color
        STRIP.show()
        
    if cpx.touch_A1:
        print("Touched A1!")        
        cpx.play_file("I_am_groot_" + str(soundNumber) + ".wav")
        if soundNumber < 4:
            soundNumber = soundNumber + 1
        else:
            soundNumber = 1

            
            
    time.sleep(0.1)
    
    