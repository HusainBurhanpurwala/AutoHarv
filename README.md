# AutoHarv

This repository is a comprehensive open-source project that demonstrates the integration of object detection and tracking using the YOLOv8 object detection algorithm and Streamlit, a popular Python web application framework for building interactive web applications. This project provides a user-friendly and customizable interface that can detect and track objects in real-time video streams.

## Demo WebApp

This app is up and running on Streamlit cloud server!!! Thanks 'Streamlit' for the community support for the cloud upload. You can check the demo of this web application on the link below.

[Auto-Harv webapp](https://autoharv.streamlit.app/)

## Tracking With Object Detection Demo

[screen-capture (1).webm](https://github.com/HusainBurhanpurwala/AutoHarv/assets/91205243/e37b2592-efba-44a8-8370-44f88958b077)


## Demo Pics

### Home page
![image](https://github.com/HusainBurhanpurwala/AutoHarv/assets/91205243/3b489701-c513-4e69-8e9e-c9ccbc2d8016)


### Page after uploading an image and object detection
![image](https://github.com/HusainBurhanpurwala/AutoHarv/assets/91205243/1a10a4e5-3168-4bf0-8ae7-97f477686445)


## Requirements

Python 3.10
YOLOv8
Streamlit

```bash
pip install ultralytics streamlit pytube
```

## Installation

- Clone the repository: git clone <https://github.com/HusainBurhanpurwala/AutoHarv.git>
- Change to the repository directory: `cd AutoHarv`
- Create `weights`, `videos`, and `images` directories inside the project.
- Download the pre-trained YOLOv8 weights from (<https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt>) and save them to the `weights` directory in the same project.

## Usage

- Run the app with the following command: `streamlit run app.py`
- The app should open in a new browser window.

### ML Model Config

- Select task (Detection, Segmentation)
- Select model confidence
- Use the slider to adjust the confidence threshold (25-100) for the model.

One the model config is done, select a source.

### Detection on images

- The default image with its objects-detected image is displayed on the main page.
- Select a source. (radio button selection `Image`).
- Upload an image by clicking on the "Browse files" button.
- Click the "Detect Objects" button to run the object detection algorithm on the uploaded image with the selected confidence threshold.
- The resulting image with objects detected will be displayed on the page. Click the "Download Image" button to download the image.("If save image to download" is selected)

## Detection in Videos

- Create a folder with name `videos` in the same directory
- Dump your videos in this folder
- In `settings.py` edit the following lines.

```python
# video
VIDEO_DIR = ROOT / 'videos' # After creating the videos folder

# Suppose you have four videos inside videos folder
# Edit the name of video_1, 2, 3, 4 (with the names of your video files) 
VIDEO_1_PATH = VIDEO_DIR / 'video_1.mp4' 
VIDEO_2_PATH = VIDEO_DIR / 'video_2.mp4'
VIDEO_3_PATH = VIDEO_DIR / 'video_3.mp4'
VIDEO_4_PATH = VIDEO_DIR / 'video_4.mp4'

# Edit the same names here also.
VIDEOS_DICT = {
    'video_1': VIDEO_1_PATH,
    'video_2': VIDEO_2_PATH,
    'video_3': VIDEO_3_PATH,
    'video_4': VIDEO_4_PATH,
}

# Your videos will start appearing inside streamlit webapp 'Choose a video'.
```

- Click on `Detect Video Objects` button and the selected task (detection/segmentation) will start on the selected video.

### Detection on RTSP

- Select the RTSP stream button
- Enter the rtsp url inside the textbox and hit `Detect Objects` button

### Detection on YouTube Video URL

- Select the source as YouTube
- Copy paste the url inside the text box.
- The detection task will start on the YouTube video url

[screen-capture.webm](https://github.com/HusainBurhanpurwala/AutoHarv/assets/91205243/20119e93-341b-48f9-90c6-c7ec1babf029)


## Acknowledgements

This app is based on the YOLOv8(<https://github.com/ultralytics/ultralytics>) object detection algorithm. The app uses the Streamlit(<https://github.com/streamlit/streamlit>) library for the user interface.

### Disclaimer

Please note that this project is intended for educational purposes only and should not be used in production environments.

**Hit star ⭐ if you like this repo!!!**
