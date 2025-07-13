import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7) 
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def fingers_up(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]
    fingers = []

    if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    for id in range(1, 5):
        if hand_landmarks.landmark[tips_ids[id]].y < hand_landmarks.landmark[tips_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

while True:
    ret, img = cap.read()
    if not ret:
        continue

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    emoji_text = ""

    if result.multi_hand_landmarks:
       for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            fingers = fingers_up(handLms)
            total_fingers = fingers.count(1)

            if total_fingers == 0:
                emoji_text = "Punch"
            elif total_fingers == 5:
                emoji_text = "Hi!"
            elif total_fingers == 1 and fingers[1] == 1:
                emoji_text = "Point"
            elif total_fingers == 2 and fingers[1] == 1 and fingers[2]==1:
                emoji_text = "Cheese!"
            elif total_fingers==10:
                emoji_text="Hi-Fi"
            elif total_fingers==10 and fingers[0]==1:
                emoji_text="Thumbs up"
            elif total_fingers==2 and fingers[1]==1 and fingers [4]==1:
                emoji_text="Swag"
            elif total_fingers==3 and fingers[2]==1 and fingers[3]==1 and fingers [4]==1:
                emoji_text="Super"
            elif total_fingers==2 and fingers[1]==1 and fingers [0]==1:
                emoji_text="Small"
            elif total_fingers==2 and fingers[0]==1 and fingers [4]==1:
                emoji_text="Call me"
            
            cv2.putText(img, emoji_text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0,0), 4)

    cv2.imshow("Emoji Tracker Deluxe™", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
