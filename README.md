# Tea Leaf Color-Based Sorting System Using Raspberry Pi

## Project Overview

This project presents a prototype tea leaf sorting system developed using a Raspberry Pi, OpenCV image processing, an iPhone camera as the image acquisition device, indicator LEDs, and a servo motor sorting mechanism. The system captures tea leaf images in real time, processes them using computer vision techniques, and classifies the tea samples based on their dominant color characteristics.

The primary objective of this prototype is to demonstrate the complete workflow of image acquisition, image processing, classification, and automated sorting. This serves as a foundation for future integration of machine learning and CNN-based tea quality classification.

---

## Features

* Real-time image acquisition using an iPhone IP camera
* Wireless communication between camera and Raspberry Pi
* OpenCV-based image processing
* HSV color space segmentation
* Tea color classification
* LED indication for detected category
* Servo motor control for automated sorting
* Expandable architecture for AI/CNN integration

---

## System Architecture

1. Camera captures tea leaf image.
2. Raspberry Pi receives image stream.
3. OpenCV processes the image.
4. Image is converted from BGR to HSV color space.
5. Color segmentation is performed using predefined HSV thresholds.
6. Color percentages are calculated.
7. Dominant tea category is identified.
8. Corresponding LED is activated.
9. Servo motor directs the tea sample into the appropriate collection box.

---

## Hardware Components

| Component      | Description                  |
| -------------- | ---------------------------- |
| Raspberry Pi 4 | Main processing unit         |
| iPhone Camera  | Wireless image acquisition   |
| Breadboard     | Circuit prototyping          |
| Green LED      | Acceptable tea indicator     |
| Yellow LED     | Medium quality tea indicator |
| Red LED        | Rejected tea indicator       |
| Servo Motor    | Sorting mechanism            |
| 220Ω Resistors | LED current limiting         |
| Jumper Wires   | Connections                  |

---

## Software Requirements

* Raspberry Pi OS
* Python 3
* OpenCV
* NumPy
* gpiozero

### Install Dependencies

```bash
sudo apt update
sudo apt install python3-opencv python3-pip -y
pip3 install numpy gpiozero
```

---

## Image Processing Methodology

### 1. Image Acquisition

An iPhone configured as an IP camera streams live video to the Raspberry Pi through a local Wi-Fi network.

### 2. Color Space Conversion

The incoming image is converted from BGR format to HSV (Hue, Saturation, Value) color space.

HSV is selected because it provides better color discrimination and is less sensitive to lighting variations compared to RGB.

### 3. Color Segmentation

Predefined HSV threshold ranges are applied to isolate different tea color regions.

The system generates binary masks representing:

* Brown tea particles
* Black tea particles
* Medium-colored tea particles

### 4. Pixel Analysis

The number of pixels belonging to each category is calculated.

The percentage distribution is determined using:

Percentage = (Detected Pixels / Total Tea Pixels) × 100

### 5. Classification

The dominant color percentage is selected as the final classification result.

### 6. Actuator Control

The Raspberry Pi activates:

* Green LED → Good quality tea
* Yellow LED → Medium quality tea
* Red LED → Rejected or over-dried tea

The servo motor rotates to direct tea into the corresponding collection container.

---

## LED Classification Logic

| LED        | Classification          |
| ---------- | ----------------------- |
| Green LED  | Acceptable Quality Tea  |
| Yellow LED | Medium Quality Tea      |
| Red LED    | Rejected/Over-Dried Tea |

---

## Future Improvements

The current implementation uses rule-based color thresholding.

Future developments include:

* CNN-based tea classification
* Tea grade identification
* Texture analysis
* Defect detection
* Impurity detection
* Industrial camera integration
* Conveyor belt automation
* Pneumatic sorting mechanism
* Real-time production monitoring

---

## Industrial Relevance

This prototype demonstrates the fundamental operation of industrial tea sorting systems. Industrial implementations typically replace:

| Prototype Component | Industrial Equivalent    |
| ------------------- | ------------------------ |
| iPhone Camera       | Industrial Vision Camera |
| Raspberry Pi        | Edge AI Computer         |
| HSV Thresholding    | CNN/Deep Learning Models |
| Servo Motor         | Pneumatic Ejector System |
| LEDs                | Industrial HMI Interface |

---

## Authors

Department of Electrical and Information Engineering
University of Ruhuna

---

## License

This project is developed for academic and research purposes.
