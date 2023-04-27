import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from c3d import *
from classifier import *
from utils.visualization_util import *
import sys;

from cameraConfig import getCameraThreshHold , getCameraModel, getBaseThreshHold;


def run_demo(video_path , vid_name):

    video_name = os.path.basename(video_path).split('.')[0]

    # read video
    video_clips, num_frames = get_video_clips(video_path)

    print("Number of clips in the video : ", len(video_clips))
    classifier_model1 = base_model_classifier(getCameraModel(camera_name, time_model));
    # build models
    feature_extractor = c3d_feature_extractor()
    classifier_model = build_classifier_model(True);
    

    print("Models initialized")

    # extract features
    rgb_features = []
    for i, clip in enumerate(video_clips):
        clip = np.array(clip)
        if len(clip) < params.frame_count:
            continue
        print(clip.shape)
        
        clip = preprocess_input(clip)
        rgb_feature = feature_extractor.predict(clip)[0]
        rgb_features.append(rgb_feature)

        print("Processed clip : ", i)

    rgb_features = np.array(rgb_features)
    print("rgb_features", rgb_features.shape)
    # bag features
    rgb_feature_bag = interpolate(rgb_features, params.features_per_bag)
    print("feature_bag", rgb_feature_bag.shape)
    
    # ensemble prediction
    # average prediction

    # classify using the trained classifier model
    
    predictions = classifier_model.predict(rgb_feature_bag) #rl
    predictions1= classifier_model1.predict(rgb_feature_bag);

    
    predictions = np.array(predictions).squeeze()
    predictions1 = np.array(predictions1).squeeze()
    
    
    predictions = extrapolate(predictions, num_frames)
    predictions1 = extrapolate(predictions1, num_frames)
    
    final_predictions = [];
    for i in range(len(predictions)):
        if(predictions[i] > getBaseThreshHold(camera_name , time_model)):
            final_predictions.append(max(predictions1[i] , predictions[i]));
        else:
            final_predictions.append(predictions[i]);


    # print(predictions , len(predictions))
    max_pred = max(predictions);
    # sys.stdout.write(str(max_pred));
    save_path = os.path.join(cfg.output_folder, vid_name );
    print("save path" ,save_path);
    # visualize predictions
    visualize_predictions(video_path, final_predictions, save_path)


#if __name__ == '__main__':
print("starting")


input_folder_path = "C:\\Users\\Asus\\Work\\anamoly detect\\Oct2022\\AnomalyDetection_CVPR18\\GUI\\public\\Inter\\";
video_name = sys.argv[1];
camera_name = sys.argv[2];
time_model = sys.argv[3];
if(camera_name == None):
    print("the camera is not provided... cannot select model");
    exit(1);
if(time_model == None):
    time_model = "day";

output_folder_path = "C:\\Users\\Asus\\Work\\anamoly detect\\Oct2022\\AnomalyDetection_CVPR18\\GUI\\public\\Outputs\\"
if(video_name != None):
    
    videoPath = os.path.join(input_folder_path , video_name);
    outputVideoPath = os.path.join(output_folder_path , video_name);
    if(not os.path.exists(os.path.join(output_folder_path , video_name.split("\\")[0]))):
        os.mkdir(os.path.join(output_folder_path , video_name.split("\\")[0]));
    


    run_demo(videoPath ,video_name);