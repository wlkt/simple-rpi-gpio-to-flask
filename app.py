from flask import Flask, render_template
import RPi.GPIO as GPIO

#GPIO 26 downto GPIO 16 for 10 bits in GPIO
pin1 = 37
pin2 = 22
pin3 = 18
pin4 = 16
pin5 = 40
pin6 = 38
pin7 = 35
pin8 = 12
pin9 = 11
pin10 = 36

GPIO.setmode(GPIO.BOARD)

# Input example 1010101010 = 682
GPIO.setup(pin1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pin3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pin5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin6, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pin7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin8, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pin9, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin10, GPIO.IN, pull_up_down = GPIO.PUD_UP)

app = Flask(__name__)

def readPins():
    sum = ( (2**0 * GPIO.input(pin1)) + (2**1 * GPIO.input(pin2)) + (2**2 * GPIO.input(pin3)) + (2**3 * GPIO.input(pin4)) + (2**4 * GPIO.input(pin5)) + (2**5 * GPIO.input(pin6)) + (2**6 * GPIO.input(pin7)) + (2**7 * GPIO.input(pin8)) + (2**8 * GPIO.input(pin9) + (2**9 * GPIO.input(pin10)) ) )
                
    return sum

@app.route('/')
def index():
    return render_template('index.html', sum=readPins(), pin1=GPIO.input(pin1), pin2=GPIO.input(pin2), pin3=GPIO.input(pin3), pin4=GPIO.input(pin4), pin5=GPIO.input(pin5), pin6=GPIO.input(pin6), pin7=GPIO.input(pin7), pin8=GPIO.input(pin8), pin9=GPIO.input(pin9), pin10=GPIO.input(pin10))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    
