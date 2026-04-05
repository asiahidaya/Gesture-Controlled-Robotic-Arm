# 🤖 Hand Gesture Controlled Robotic Arm

A real-time robotic arm system controlled using hand gestures detected through computer vision. This project integrates Python-based hand tracking with Arduino-controlled servo motors to replicate human finger movements.

---

## 🚀 Features

- ✋ Real-time hand tracking using MediaPipe
- 🎯 Accurate finger detection (Thumb to Pinky)
- 🔄 Live gesture-to-hardware mapping
- 🔌 Serial communication between Python and Arduino
- 🤖 Servo motor control for robotic hand movement

---

## 🛠 Tech Stack

- **Programming Language:** Python, Arduino (C++)
- **Libraries:** OpenCV, MediaPipe, PySerial
- **Hardware:** Arduino, Servo Motors (5), Webcam

---

## ⚙️ How It Works

1. Webcam captures live video feed
2. MediaPipe detects hand landmarks
3. Finger positions (UP/DOWN) are calculated
4. Python sends commands via serial communication
5. Arduino receives commands and moves servo motors
6. Robotic hand mimics real-time gestures

---


---

## 🔌 Hardware Requirements

- Arduino Board (Uno/Nano)
- 5 Servo Motors
- Jumper Wires
- USB Cable
- Webcam

---

## 🧠 Key Concepts Used

- Computer Vision
- Hand Landmark Detection
- Real-time Processing
- Serial Communication
- Embedded Systems

---


---

## ⚠️ Important Notes

- Ensure correct COM port in Python code
- Keep proper lighting for better hand detection
- Adjust servo angles based on hardware setup

---


## 🚀 Future Improvements

- Add gesture customization
- Improve finger detection accuracy
- Wireless control using Bluetooth/WiFi
- Add full robotic arm (not just fingers)

---

## 🙋‍♀️ Author

**Asia Hidaya**  
GitHub: https://github.com/asiahidaya
