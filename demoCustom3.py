import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from c3d import *
from classifier import *
from utils.visualization_util import *
import sys;


def run_demo(video_path):

    video_name = os.path.basename(video_path).split('.')[0]

    # read video
    video_clips, num_frames = get_video_clips(video_path)

    print("Number of clips in the video : ", len(video_clips))

    # build models
    feature_extractor = c3d_feature_extractor()
    classifier_model = base_model_classifier(); 
    # build_classifier_model2()
    classifier_model2 = build_classifier_model(True);

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
    predictions1 = classifier_model2.predict(rgb_feature_bag)

    
    predictions = np.array(predictions).squeeze()
    predictions1= np.array(predictions1).squeeze()
    
    predictions = extrapolate(predictions, num_frames)
    predictions1 = extrapolate(predictions1, num_frames)
    
    final_predictions = [];
    for i in range(len(predictions)):
        if(predictions1[i] > 0.10):

            final_predictions.append(max(predictions1[i] , predictions[i]));
        else:
            final_predictions.append(predictions1[i]);

    print(predictions);
    
    save_path = os.path.join(cfg.output_folder, video_name + '.mp4')
    # visualize predictions
    visualize_predictions1(video_path, predictions, save_path)
    visualize_predictions1(video_path, predictions1, save_path)
    
    visualize_predictions1(video_path, final_predictions, save_path)
    


def getTheFrame(video_path , frame_no):
    cap = cv2.VideoCapture(video_path)
    counter = 0;
    while(cap.isOpened()):
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            if(counter == frame_no):
                return frame;
            counter+=1;
            # Display the resulting frame
            
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        # Break the loop
        else: 
            break
        
# When everything done, release the video capture object
    cap.release()
 
# Closes all the frames
    cv2.destroyAllWindows()
    return None;
    pass

#if __name__ == '__main__':
print("starting")

# input_folder_path = "C:\\Users\\Asus\\Work\\anamoly detect\\Oct2022\\AnomalyDetection_CVPR18\\GUI\\public\\Files\\";
# input_folder_path = "C:\\Users\\Asus\\Desktop\\FYP things\\Anomaly_Clipped_Videos_Anomaly_Only\\outside_sports\\"
input_folder_path = "C:\\Users\\Asus\\Desktop\\FYP things\\Anomaly_Clipped_Videos_Anomaly_Only\\front_Garden_anomaly\\"



video_name = sys.argv[1];



if(video_name != None):
     
    videoPath = input_folder_path + video_name;
    print(videoPath);

    run_demo(videoPath);