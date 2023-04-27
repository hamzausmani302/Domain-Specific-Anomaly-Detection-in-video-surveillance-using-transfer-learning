import configuration as cfg;
import numpy as np;
from utils.visualization_util import *
from utils.video_util import *;
from c3d import *;
import tensorflow as tf;
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
  tf.config.experimental.set_memory_growth(gpu, True)

SAVE_PATH= "./EXTRACTED_FEATURES/";

video_clips, num_frames = get_video_clips(cfg.sample_video_path)
feature_extractor = c3d_feature_extractor()
    
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
    
print(rgb_features.shape);
with open(SAVE_PATH+ "test.npy", "wb") as f:
     np.save(f, rgb_features)
f.close()




