import cv2
import os;  
import time;  

start = 0;
end = 0;
total_frames = 0;
t = "abnormal";


def runVideo(filename):
        # define a video capture object
    start = 0;
    end = 0;
    total_frames = 0;
    t = "abnormal";

    vid = cv2.VideoCapture(filename)
    total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    i = 0;
    print(total_frames)
    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        if(ret == False):
            break;
        # Display the resulting frame
        cv2.putText(frame , "frame: "+str(i) , (50,50) , cv2.FONT_HERSHEY_SIMPLEX , 1 , (0,255,255) , 2 ,cv2.LINE_4);
        
        cv2.imshow('frame', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
       
        if cv2.waitKey(2) & 0xFF == ord('r'):
            time.sleep(2);
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        i+=1;
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

# runVideo("../input/video_276144_5.mp4");
# for f in os.listdir("../input"):
#     vid = cv2.VideoCapture(os.path.join("../input" , f))
#     total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
#     print(f , total_frames);

import sys;
vid = cv2.VideoCapture("C:\\Users\\Asus\\Desktop\\FYP things\\Anomaly_Clipped_Videos_Normal_Only\\outside sports\\day\\{}.mp4".format(sys.argv[1]))
total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
print("video" , total_frames);