import classifier
import configuration as cfg
import numpy as np
import os

def load_test_set(videos_path, videos_list):
    feats = []
    
    for vid in videos_list:
        if(".txt" not in vid):
            vid_path = os.path.join(videos_path, vid)
            print(vid_path)
            
            feat = np.load(vid_path ,allow_pickle=True)
            feats.append(feat)

    feats = np.array(feats)
    return feats

# classifier_model = classifier.build_classifier_model(True);
classifier_model = classifier.base_model_classifier();
vid_list = os.listdir(cfg.test_features_path)
vid_list.sort()

test_set = load_test_set(cfg.test_features_path, vid_list)

for filename, example in zip(vid_list, test_set):
    # print(filename , example)
    predictions_file = filename[:-4] + '.npy'
    pred_path = os.path.join(cfg.preds_path, predictions_file)
    pred = classifier_model.predict_on_batch(example)
    # print(pred);
    with open(pred_path, "wb") as f:
        np.save(pred_path, pred, allow_pickle=True)


