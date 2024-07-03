from flask import Flask, Response
import cv2
import mediapipe as mp

app = Flask(__name__) # instance creation

#Initializing mp and loading models

mp_hands = mp.solutions.hands # module
mp_drawings = mp.solutions.drawing_utils
hands = mp_hands.Hands()  # model

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def gen_frames():
    print("Starting video capture...")
    video = cv2.VideoCapture(0)

    while True:
        success, frame = video.read()
        print("Frame captured:", success)

        if not success:
            print("Failed ")
            break
        else:
            grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(grey_img)
            
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            
            
            results = hands.process(frame)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawings.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/video_feed')
def video_feed():
    print("Starting video feed")
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)  
