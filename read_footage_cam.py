
from re import sub
import cv2
import subprocess;
import os;
import sys;

# cam = cv2.VideoCapture("http://localhost/video")

# cv2.namedWindow("test")

# img_counter = 0

# while True:
#     ret, frame = cam.read()
#     if not ret:
#         print("failed to grab frame")
#         break
#     cv2.imshow("test", frame)

#     k = cv2.waitKey(1)
#     if k%256 == 27:
#         # ESC pressed
#         print("Escape hit, closing...")
#         break
#     elif k%256 == 32:
#         # SPACE pressed
#         img_name = "opencv_frame_{}.png".format(img_counter)
#         cv2.imwrite(img_name, frame)
#         print("{} written!".format(img_name))
#         img_counter += 1

# cam.release()

# cv2.destroyAllWindows()


duration = 20;
def fetchAndRunInference(i):
    # -f dshow -s 320x240 -r 30 

    cmd1 = "ffmpeg -f dshow  -t {} -vcodec mjpeg -i video=\"USB2.0 HD UVC WebCam\" ./public/Files/output{}.mp4".format(duration , i);
    res = subprocess.call(cmd1 , shell=True);
    if(res == 0):
        print("successfully retreived vdeos");
    else:
        print("error occured");
    #run inference on video

    run_cmd = "python ../demoLive.py output{}.mp4 frontGate".format(i)
    pr = subprocess.call(run_cmd , shell=False);
    
# for i in range(2):
#     fetchAndRunInference(i);

if(len(sys.argv) > 0):

    index = sys.argv[1];
else:
    index = 0;



fetchAndRunInference(str(index));

