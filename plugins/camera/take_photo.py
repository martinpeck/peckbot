import picamera
import time
outputs = []
files = []
crontable = []

def process_message(data):

    if data['channel'].startswith("D"):

        if data['text'] == "take photo":
            with picamera.PiCamera() as camera:
                camera.resolution = (1024,768)
                time.sleep(2)
                camera.capture("./capture/image.jpg")
            files.append([data['channel'], "./capture/image.jpg" ])
            outputs.append([data['channel'], "Photo taken and available in #photos"])

        if data['text'] == "take video":
            with picamera.PiCamera() as camera:
                camera.resolution = (640,480)
                camera.start_recording('./capture/video.mjpeg', format='mjpeg')
                camera.wait_recording(10)
                camera.stop_recording()
            files.append([data['channel'], "./capture/video.mjpeg" ])
            outputs.append([data['channel'], "Video shot and available in #photos"])
            
        if data['text'] == "camera help":
            outputs.append([data['channel'], "HELP GOES HERE"])

        if data['text'] == "camera status":
            outputs.append([data['channel'], "STATUS GOES HERE"])

        if data['text'] == "start timed photo":
            outputs.append([data['channel'], "I'll start taking photos every 30 seconds"])
            crontable.append([30,"timed_photo"])

        if data['text'] == "stop timed photo":
            outputs.append([data['channel'], "I'll stop taking photos every 30 seconds"])
            crontable = []


def timed_photo():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024,768)
        time.sleep(2)
        camera.capture("./capture/timed_photo.jpg")
    files.append(["C0H2MRJPM","./capture/timed_photo.jpg"])
