from flask import Flask, render_template
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pinVal1=(str(GPIO.input(23))), pinVal2=(str(GPIO.input(24))))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    
