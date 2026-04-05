import serial
import time

arduino = serial.Serial('COM6', 9600)
time.sleep(2)

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

tip_ids = [4, 8, 12, 16, 20]

prev_data = ""

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)

    result = detector.detect(mp_image)

    fingers = [0, 0, 0, 0, 0]

    if result.hand_landmarks:

        for i, hand_landmarks in enumerate(result.hand_landmarks):

            lm_list = []
            h, w, _ = img.shape

            for id, lm in enumerate(hand_landmarks):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

            hand_label = result.handedness[i][0].category_name

            # 👍 Thumb
            if hand_label == "Right":
                if lm_list[4][1] > lm_list[3][1]:
                    fingers[0] = 1
            else:
                if lm_list[4][1] < lm_list[3][1]:
                    fingers[0] = 1

            # Other fingers
            for j in range(1, 5):
                if lm_list[tip_ids[j]][2] < lm_list[tip_ids[j] - 2][2]:
                    fingers[j] = 1

    # 🔥 Send all fingers
    data = ''.join(map(str, fingers))

    if data != prev_data:
        arduino.write((data + "\n").encode())
        prev_data = data

    cv2.putText(img, f'Fingers: {data}', (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Gesture → 5 Servos", img)

    if cv2.waitKey(1) & 0xFF in [27, ord('q')]:
        break

cap.release()
cv2.destroyAllWindows()