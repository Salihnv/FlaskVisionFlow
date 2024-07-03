# FlaskVisionFlow

FlaskVisionFlow is a real-time face and hand detection application integrated with Flask for online streaming. The application uses OpenCV for face detection and MediaPipe for hand detection, providing a seamless and efficient streaming experience.

## Features

- Real-time face detection using OpenCV
- Real-time hand detection using MediaPipe
- Integrated with Flask for online video streaming
- User-friendly and efficient performance


## Code Overview: `app.py`

`app.py` is the main file that sets up the Flask application and integrates the real-time video streaming with face and hand detection.

### Imports necessary libraries:

- Flask
- Response from Flask
- OpenCV
- MediaPipe

### Initializes:

- MediaPipe for hand detection
- OpenCV for face detection

### Functions:

- Defines `gen_frames()` function to capture video frames, detect faces and hands, and encode the frames for streaming.
- Defines Flask routes to handle video streaming.

## Requirements

To run FlaskVisionFlow, ensure you have the following dependencies installed:

- Flask
- OpenCV
- MediaPipe

You can install these dependencies using the following command:

```bash
pip install flask opencv-python mediapipe
