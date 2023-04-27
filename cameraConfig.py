import configuration as cfg;
import os;
cameras = {
    "frontGate" : {"day" : {"model" : "frontGate-day.mat" , "base" : 0.2,  "threshhold" : 0.50} , "night" :{ "model" : "" , "base" : 0.2 , "threshhold":0.49}},
    "outsideSports" : {"day" : {"model" : "model_1_1.mat" ,"base" : 0.1, "threshhold" : 0.4} , "night" :{ "model" : "", "base" : 0.2 , "threshhold":0.4}},
    "basement" : {"day" : {"model" : "model_1_1.mat" ,"base" : 0.2, "threshhold" : 0.2} , "night" :{ "model" : "", "base" : 0.2 , "threshhold":0.49}},
}

def getWhen(when):
    lower_case_when = when.lower();
    return lower_case_when;

def getCameraModel(camera , when="day"):
    print(cameras[camera][getWhen(when)]["model"] + " loaded")
    return os.path.join(cfg.models_folder_path , cameras[camera][getWhen(when)]["model"])

def getCameraThreshHold(camera , when="day"):
    try:
        return cameras[camera][getWhen(when)]["threshhold"];
    except:
        return 0.5

def getBaseThreshHold(camera , when="day"):
    try:
        return cameras[camera][getWhen(when)]["base"]
    except:
        return 0.1

