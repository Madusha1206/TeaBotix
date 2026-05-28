# Tea Leaf Image Classification System Using Raspberry Pi and Computer Vision

## Project Overview

This project presents a real-time tea leaf image classification system developed using a Raspberry Pi and an iPhone camera. The system captures images of tea leaves through a wireless camera stream and performs image processing to classify tea samples based on their visual color characteristics.

The objective of this prototype is to establish a complete image acquisition and processing pipeline for tea leaf analysis, which can later be extended to advanced machine learning and deep learning techniques such as Convolutional Neural Networks (CNNs).

---

## System Description

The iPhone is configured as a wireless IP camera and streams live video to the Raspberry Pi through a local Wi-Fi network. The Raspberry Pi receives the video stream and processes each image frame in real time using the OpenCV computer vision library.

The captured images undergo several image processing stages including preprocessing, color space conversion, segmentation, feature extraction, and classification. The final output is the identification of the dominant tea leaf category based on color characteristics.

---

## Hardware Components

* Raspberry Pi 4
* iPhone Camera (IP Camera)
* Wi-Fi Network Connection

---

## Software Components

* Python 3
* OpenCV
* NumPy
* Raspberry Pi OS

---

## Image Processing Methodology

### 1. Image Acquisition

The iPhone camera continuously captures images and transmits them to the Raspberry Pi over a wireless network. This provides a live video stream for real-time processing.

### 2. Image Preprocessing

Each incoming image frame is resized to a standard resolution to reduce computational complexity and improve processing speed. Preprocessing ensures consistent image dimensions for subsequent operations.

### 3. Color Space Conversion

The captured image is initially represented in the BGR color format used by OpenCV. To improve color analysis, the image is converted to the HSV (Hue, Saturation, Value) color space.

HSV is selected because it separates color information from brightness information, making color detection more robust under varying illumination conditions.

### 4. Color Segmentation

Specific HSV threshold ranges are applied to isolate different tea leaf color regions. Binary masks are generated to identify pixels belonging to particular color categories.

In each mask:

* White pixels represent detected tea regions.
* Black pixels represent background or non-target regions.

This segmentation process allows the system to distinguish tea samples based on their dominant visual appearance.

### 5. Feature Extraction

After segmentation, the system calculates the number of pixels belonging to each detected color region. These pixel counts are used as features for classification.

The percentage contribution of each color category is determined using:

Percentage = (Detected Color Pixels / Total Detected Tea Pixels) × 100

### 6. Tea Leaf Classification

The dominant color percentage is used to determine the classification result. The tea sample is assigned to the category with the highest detected percentage.

This approach provides a simple but effective rule-based classification mechanism suitable for prototype development.

### 7. Real-Time Visualization

The processed image is displayed in real time, allowing visualization of:

* Original camera feed
* Segmented color regions
* Classification results
* Detected tea leaf areas

This enables immediate verification of the classification performance.

---

## Current Limitations

* Classification is based only on color information.
* Performance may be affected by lighting variations.
* Background objects with similar colors may influence results.
* Texture and shape features are not considered.

---

## Future Development

The current HSV-based classification serves as the initial stage of the project. Future work will focus on developing a CNN-based classification model capable of identifying tea varieties and quality grades using multiple image features, including:

* Color
* Texture
* Shape
* Surface appearance
* Defect characteristics

The CNN model will be trained using a dedicated tea leaf image dataset to achieve higher classification accuracy and improved robustness under varying environmental conditions.

---

## Conclusion

This project successfully demonstrates a real-time tea leaf image processing system using a Raspberry Pi and an iPhone camera. The implemented pipeline includes image acquisition, preprocessing, HSV color-based segmentation, feature extraction, and classification, providing a strong foundation for future AI-based tea quality assessment systems.
