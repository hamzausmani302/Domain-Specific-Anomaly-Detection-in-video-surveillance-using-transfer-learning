# DOMAIN SPECIFIC ANOMALY DETECTION IN VIDEO SURVEILLANCE USING TRANSFER LEARNING


Implementation of [Real-world Anomaly Detection in Surveillance Videos](https://arxiv.org/pdf/1801.04264.pdf) paper from CVPR 2018.
Original implementation from authors is [here](https://github.com/WaqasSultani/AnomalyDetectionCVPR2018).

Download C3D sports-1m weights from [here](https://github.com/adamcasson/c3d/releases/download/v0.1/sports1M_weights_tf.h5) and
save them to 'trained_models' folder as 'c3d_sports1m.h5'.

Run demo.py to run the code on the demo video in 'input' folder. Visualization of the predictions from the model is saved in 'output' folder.

#### Libraries Used

- Keras : 2.2.0
- Tensorflow : 1.10.1
- Numpy : 1.14.5
- OpenCV : 3.3.0.10
- Scipy : 0.19.1
- Matplotlib : 2.0.2

## Authors

- [Dr Muhammad Atif Tahir](https://scholar.google.at/citations?user=tBKYSE0AAAAJ&hl=en)    (Supervisor)
- [Hamza Usmani]()
- [Ibad Saleem]()
- [Abdul Rehman]()



## Installation


Install Anaconda

https://www.anaconda.com/download/
(Make sure anazonda path variable is set)

Verify conda 

```bash
conda --version
```


Clone the project

```bash
  git clone https://github.com/hamzausmani302/Domain-Specific-Anomaly-Detection-in-video-surveillance-using-transfer-learning.git
```

Go to the project directory

```bash
  cd Domain-Specific-Anomaly-Detection-in-video-surveillance-using-transfer-learning
```

Load conda environment and install dependencies

```bash
  conda env create -f testEnv.yml
```
Install nodejs from https://nodejs.org/download/release/v16.20.0

We have testig on node 16 other version will also work work , but install 16 for safe side.


&nbsp;
&nbsp;
---
&nbsp;

(Optional but important GPU is required)
The command above wiil setup cudatoolkit and cudnn but if GPU is still not detected, install cuda software and cudnn library based on the graphic card version.
Link for CUDA setup: 

https://medium.com/geekculture/install-cuda-and-cudnn-on-windows-linux-52d1501a8805

Check GPU is setup and detected






## Usage/Examples

```python
import tensorflow as tf

if tf.test.is_built_with_cuda() and tf.test.is_gpu_available():
    print("TensorFlow is running with GPU support.");
else:
    print("TensorFlow is running on CPU.");
```

or run the testModel.py file


## Run Application

1. Move to root folder of the project in Anaconda Prompt   (open Anaconda Prompt and navigate to the root folder)

2. Navigate to the GUI folder 
```bash
    cd GUI
    npm install
    node index.js
``` 


## Features

- running predictions on videos and extracting anomalous frames.
- running predictions on videos and generating graphical frame level predictions.
- running application on live feed
- Context Switching based on camera as well as day and night


## Demo

[![Watch the video](https://i.ytimg.com/vi/ulkKKtzfgFA/maxresdefault.jpg)](https://drive.google.com/file/d/1FvyD3dQsXR1BrSHcqWGHQK6z3OXvwoUs/view?usp=share_link
)


## Project Files


GUI/

    Controllers/
    public/
        assets/ - contain static data for websites
        Files/  - contains files uploaded by application
        Inter/  - Contains file after being broken down into sub files
        Outputs/  - outputs of the prediction on these files
        Views/ - contains html file and javascript code for the file
    Routers/
        router.js  - api routes for the application
    scripts/
    serverUtils/
        cameraUtil.js  - camera functions
        fileUtils.js  - library for file related operations
        utils.js - general operations library
    backupindex.js
    config.js   -  application configuration
    index.js  -   contains business logic for running predictions.. brain of application
    package.json

NOTE_FRAMES/

    framestream.py - display videos with frame number
preds_path/         - stores predictions from predict_test_set.py file for evaluating model

testFeatures/   - store test features after extration.

trained_models/  - store models
    
    sports1M_weights_tf.h5
    frontGate-day.mat
utils/  - general functions used by the python files for prediction.

c3d.py  -  C3D model file

classifer.py  - contains the predictor network.

demoCustom2.py - script for graph video prediction used by index.js file

demoCustom3.py

demoCustom4.py - script for ouutputting frame image predictions used by index.js file

clip_maker.py

clip_maker2.py

clip_maker3.py - break videos into 30 seconds clips and save them in Inter/ Folder.


feature_extract.py - extract C3D features for prediction.


read_footage_cam.py -  script used during live prediction.

temporal-annotations.txt - temporal file for evalurating metrics

predict_test_set.py - test the features and output predictions in pred_path folder


configuration.py  - configuration for the python files


cameraConfig.json - centralized view of configuration of cameras

cameraConfig.py - retreiver functions from cameraConfig.json file for use by the application

