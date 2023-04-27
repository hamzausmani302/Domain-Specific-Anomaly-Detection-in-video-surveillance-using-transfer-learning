import sys;
import os

if(len(sys.argv)  < 2):
    print("arguments not privided");
source_video=  sys.argv[0];
dest_video = sys.argv[1];
print(os.environ['CONDA_DEFAULT_ENV']   , source_video , dest_video);