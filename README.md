# Hand Gesture-Controlled Robotic Arm 🤖✋

An interactive system that controls a robotic arm using real-time hand gestures.
This project combines **Computer Vision + Arduino + Servo Motors** to create a contactless control system.

---

## 🧠 Overview

This project enables users to control a robotic arm using hand gestures captured through a camera.
The gestures are processed using Python, and commands are sent to an Arduino, which controls the servo motors of the robotic arm.

---

## ⚙️ System Architecture

```
Hand Gesture → Camera  
        ↓  
Python (OpenCV / MediaPipe)  
        ↓  
Serial Communication  
        ↓  
Arduino  
        ↓  
Servo Motors (Robotic Arm)
```

---

## 🔧 Hardware Used

* Arduino Uno
* Servo Motors (for arm movement)
* Robotic Arm Structure
* Jumper Wires
* Breadboard
* Webcam / External Camera

---

## 💻 Software Used

* Python
* OpenCV
* MediaPipe (for hand tracking)
* Arduino IDE

---

## ✨ Features

* ✋ Real-time hand gesture detection
* 🤖 Controls robotic arm movements
* 🔄 Smooth and responsive motion
* 🔌 Serial communication between Python and Arduino
* 🧠 Multi-domain integration (AI + Embedded Systems)

---

## ⚙️ How It Works

1. The camera captures live video of hand gestures
2. Python processes the video using OpenCV / MediaPipe
3. Hand landmarks are detected and interpreted
4. Corresponding commands are generated
5. Commands are sent via serial communication
6. Arduino receives the data
7. Servo motors move the robotic arm accordingly

---

## 📸 Screenshots

*(Add images here)*

* Gesture detection
* Robotic arm setup
* Movement output

---

## 🛠 Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/asiahidaya/Gesture-Controlled-Robotic-Arm.git
cd Gesture-Controlled-Robotic-Arm
```

### 2. Install Python dependencies

```
pip install opencv-python mediapipe pyserial
```

### 3. Upload Arduino Code

* Open Arduino IDE
* Upload the `.ino` file to your Arduino board

### 4. Run Python Script

```
python main.py
```

## Why I built this
To explore real-time human-computer interaction and integrate computer vision with embedded systems for intuitive control.

---

## 📌 Applications

* 🤖 Robotics and Automation
* 🏥 Assistive Technology
* 🎮 Gesture-based Control Systems
* 🧠 Human-Computer Interaction

---

## 🚀 Future Improvements

* Add wireless communication (Bluetooth/WiFi)
* Improve gesture recognition accuracy
* Add more complex arm movements
* Integrate with web dashboard (IoT)


---
