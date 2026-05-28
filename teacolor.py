import cv2
import numpy as np
import time
from gpiozero import LED, AngularServo

url = "http://*****:*****@192.168.8.105:8081/video"

green_led = LED(17)
brown_led = LED(27)
black_led = LED(22)

servo = AngularServo(18, min_angle=0, max_angle=180)

GREEN_POS = 30
BROWN_POS = 90
BLACK_POS = 150

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Camera not opened")
    exit()

def all_leds_off():
    green_led.off()
    brown_led.off()
    black_led.off()

def sort_leaf(color):
    all_leds_off()

    if color == "GREEN":
        green_led.on()
        servo.angle = GREEN_POS
        print("GREEN leaf → Box 1")

    elif color == "BROWN":
        brown_led.on()
        servo.angle = BROWN_POS
        print("BROWN leaf → Box 2")

    elif color == "BLACK":
        black_led.on()
        servo.angle = BLACK_POS
        print("BLACK leaf → Box 3")

    time.sleep(1.5)
    all_leds_off()
    servo.angle = 90

last_sort_time = 0
delay_between_sorts = 3

while True:
    ret, frame = cap.read()

    if not ret:
        print("Frame not received")
        break

    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    green_mask = cv2.inRange(hsv, np.array([35, 40, 40]), np.array([85, 255, 255]))
    brown_mask = cv2.inRange(hsv, np.array([5, 50, 20]), np.array([25, 255, 180]))
    black_mask = cv2.inRange(hsv, np.array([0, 0, 0]), np.array([180, 255, 50]))

    green_pixels = cv2.countNonZero(green_mask)
    brown_pixels = cv2.countNonZero(brown_mask)
    black_pixels = cv2.countNonZero(black_mask)

    total = green_pixels + brown_pixels + black_pixels

    if total > 2000:
        green_percent = green_pixels / total * 100
        brown_percent = brown_pixels / total * 100
        black_percent = black_pixels / total * 100

        if green_percent > brown_percent and green_percent > black_percent:
            detected = "GREEN"
        elif brown_percent > black_percent:
            detected = "BROWN"
        else:
            detected = "BLACK"

        cv2.putText(frame, detected, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        current_time = time.time()

        if current_time - last_sort_time > delay_between_sorts:
            sort_leaf(detected)
            last_sort_time = current_time

    cv2.imshow("Tea Leaf Sorting", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
all_leds_off()
servo.angle = 90
