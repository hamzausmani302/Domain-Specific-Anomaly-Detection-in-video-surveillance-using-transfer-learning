import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from c3d import *
from classifier import *
from utils.visualization_util import *
import sys;


def run_demo(video_path , vid_name):

    video_name = os.path.basename(video_path).split('.')[0]

    # read video
    video_clips, num_frames = get_video_clips(video_path)

    print("Number of clips in the video : ", len(video_clips))

    # build models
    feature_extractor = c3d_feature_extractor()
    classifier_model = build_classifier_model1(camera_name)

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
    
    predictions = classifier_model.predict(rgb_feature_bag)

    
    predictions = np.array(predictions).squeeze()

    
    predictions = extrapolate(predictions, num_frames)
    sys.stdout.flush()
    max_pred = max(predictions);
    with open(cfg.INTERMEDIATE_BUFFER , "w") as f:
        f.write(str(max_pred));

    sys.stdout.write(str(max_pred));
    save_path = os.path.join(cfg.output_camera_live_path, vid_name )
    # print("save path" ,save_path);
    # visualize predictions
    # visualize_predictions(video_path, predictions, save_path)


#if __name__ == '__main__':
print("starting")


input_folder_path = "C:\\Users\\Asus\\Work\\anamoly detect\\Oct2022\\AnomalyDetection_CVPR18\\GUI\\public\\Files\\";
video_name = sys.argv[1];
camera_name = sys.argv[2];
if(camera_name == None):
    print("the camera is not provided... cannot select model");
    exit(1);

output_folder_path = "C:\\Users\\Asus\\Work\\anamoly detect\\Oct2022\\AnomalyDetection_CVPR18\\GUI\\public\\Outputs\\Camera"
if(video_name != None):
    
    videoPath = os.path.join(input_folder_path , video_name);
    # outputVideoPath = os.path.join(output_folder_path , "Camera");
    if(not os.path.exists(output_folder_path )):
        os.mkdir(output_folder_path );
    


    run_demo(videoPath ,video_name);