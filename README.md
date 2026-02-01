# Hand Gesture (Emoji) Detection using OpenCV and MediaPipe

## 📌 Project Overview
This project is a **real-time hand gesture detection system** that identifies different hand gestures using a webcam and displays the corresponding gesture name or emoji on the screen.

The system captures live video input, detects hand landmarks, analyzes finger positions, and classifies gestures based on the number and combination of fingers raised.

---

## 🎥 How It Works
1. Accesses the user's webcam using OpenCV
2. Detects hand landmarks using MediaPipe Hands
3. Determines which fingers are raised
4. Classifies the hand gesture based on predefined rules
5. Displays the detected gesture as text on the screen in real time

---

## 🧠 Gesture Detection Logic

### 🔹 Finger Detection
- MediaPipe provides predefined hand landmark indices
- Fingers (index, middle, ring, pinky) are detected using a standard finger-up logic
- **Thumb detection is handled separately** due to its unique orientation

### 🔹 Thumb Detection
- A custom function is used to detect whether the thumb is raised
- The thumb is considered "up" if its landmark length exceeds a defined threshold
- This is calculated using landmark coordinates provided by MediaPipe

---

## ✋ Finger State Representation
- A list is created to track finger states
- Each index represents a finger:
  - Index 0 → Thumb
  - Index 1 → Index Finger
  - Index 2 → Middle Finger
  - Index 3 → Ring Finger
  - Index 4 → Pinky
- Value `1` indicates finger is up, `0` indicates finger is down

---

## 🖐️ Gesture Classification
Gestures are identified based on:
- Total number of fingers raised
- Specific combinations of raised fingers

### Examples:
- **0 fingers up** → Punch
- **5 fingers up** → High Five
- **1 finger up (Index)** → Pointing
- **2 fingers up (Index + Middle)** → Peace / Cheese
- **Thumb only** → Thumbs Up
- Other combinations → Swag, Call Me, Super, etc.

These rules are manually defined to map finger patterns to gestures.

---

## 🛠️ Technologies Used
- Python
- OpenCV
- MediaPipe
- NumPy

---

## 🎯 Features
- Real-time hand gesture recognition
- Custom thumb detection logic
- Multiple gesture support
- Live webcam processing
- On-screen gesture display

---

## 🚀 Future Enhancements
- Add gesture-to-emoji mapping
- Improve gesture accuracy
- Support multiple hands
- Integrate gesture-based controls
- Optimize performance for low-end devices

---

## 🏁 Conclusion
This project demonstrates real-time computer vision and hand landmark analysis using OpenCV and MediaPipe. It highlights custom gesture logic implementation and effective use of finger detection techniques to classify multiple hand gestures accurately.
