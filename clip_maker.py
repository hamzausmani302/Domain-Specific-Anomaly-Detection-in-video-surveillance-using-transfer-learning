
from asyncio import subprocess

import numpy as np;
from utils.video_util import get_video_clips , get_video_frames;
from utils.array_util import sliding_window;
import parameters as params;
from PIL import Image;
import cv2;
import os;
import subprocess;
import math;
from moviepy.editor import *


#change these variables for video cutting
INPUT_VIDEO_DIR = "./input";
OUTPUT_DIR_VIDEO= "./output_clips";
OUTPUT_VIDEO_BASE_NAMES = "output";             # the output video name must start with the following nme 

###########3




VIDEO_PATH = "./input/Explosion008_x264.mp4";
OUTPUT_DIR ="";
TOTAL_DIVISIONS =5;
def load_video(path):
    
    
    return  get_video_frames(path);
    
def getFrames(frame_count):
    return int(frame_count/TOTAL_DIVISIONS);

def divide_video(frames):
    #print(len(frames));
    total_frames = len(frames);
    print("each frame")
    clips = sliding_window(frames, getFrames(total_frames) , getFrames(total_frames));
    print(np.array(clips[0]).shape)
    return clips;


def make_video(frames):
    height = params.frame_height
    width = params.frame_width
    print(len(frames));
    fps = int(len(frames)/(TOTAL_DIVISIONS*10));
    video_filename = 'output.avi'
    video_out = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),cv2.VideoCapture(VIDEO_PATH).get(cv2.CAP_PROP_FPS), (width, height)) 
    for frame in frames:
        img = Image.fromarray(frame);
        video_out.write(frame)
    cv2.destroyAllWindows();
    video_out.release()
    # new frame after each addition of water
    # for i in range(10):
    #     random_locations = np.random.random_integers(200,450, size=(200, 2))
    #     for item in random_locations:
    #         water_depth[item[0], item[1]] += 0.1
    #         #add this array to the video
    #         gray = cv2.normalize(water_depth, None, 255, 0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    #         gray_3c = cv2.merge([gray, gray, gray])
    #         out.write(gray_3c)

    # close out the video writer
    # out.release()





def run_video():
    video_frames = load_video(VIDEO_PATH);

    #print(np.array(video_frames).shape);

    clips = divide_video(video_frames);
    print(len(clips[0]))
    make_video(clips[0]);

    pass

def convert_into_format(number):
    if(number<10):
        return "0"+str(number);
    return str(number);

def get_duration_video(videopath):
    clip = VideoFileClip(videopath);
    seconds = math.floor(clip.duration)
    return seconds;

def convert_seconds_to_format(seconds):
    s = seconds;
    hours = math.floor(seconds/3600);
    s -= (hours * 3600);
    minutes = math.floor(s/60);
    s -= (minutes*60)

    hours_str = convert_into_format(hours);
    minutes_str = convert_into_format(minutes);
    seconds_str= convert_into_format(s);
    return "{}:{}:{}".format(hours_str , minutes_str , seconds_str);


    pass
def break_video_into_small_videos_from_utils(input_folder_path ,video_name , output_folder_path , basename , start=0 , duration=30, video_tag=0):
    
    cmd = ["ffmpeg" , 
    "-ss" , convert_seconds_to_format(start) , 
    "-t" , str(duration) , 
    "-i" , "./{}/{}".format(input_folder_path,video_name),
    "-acodec" , "copy",
    "./{}/{}.mp4".format(output_folder_path , basename.split(".")[0]+ str(start) )
    ];
    p = subprocess.Popen(cmd , shell=True);
    p.wait();
#print(
# np.array(split_frames[0]).shape);
#make_video(split_frames[0])
def break_video_into_clips(input_folder_path ,video_name , output_folder_path , basename):
    start = 0;
    duration = 10;
    end = get_duration_video(input_folder_path + "/" + video_name);
    folder_path =output_folder_path + "/" + video_name.split(".")[0]; 
    if(not os.path.exists(folder_path)):

        os.mkdir(folder_path);
    while(start < end):

        break_video_into_small_videos_from_utils(input_folder_path , video_name , folder_path ,basename ,start , duration  );
        start += duration;


video_n = os.listdir(INPUT_VIDEO_DIR);

for video in video_n:
    
    print("preapring video {}".format(video));
    break_video_into_clips( INPUT_VIDEO_DIR, video , OUTPUT_DIR_VIDEO , OUTPUT_VIDEO_BASE_NAMES);

