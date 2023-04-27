const fs = require("fs");
const path = require("path");
const { exec } = require("child_process");
const { execSync } = require("child_process");
const { spawn } = require("child_process");

const run_live_prediction = async (camera, i) => {
  let promise = new Promise((resolve, reject) => {
    exec(
      `conda run -n testEnv python ../read_footage_cam.py ${i} ${camera}`,
      (error, stdout, stderr) => {
        if (error) {
          reject(error);
          return;
        }
        resolve(stdout);
      }
    );
  });
  return promise;
};

const detectionOnVideo = async (message, filename, cam, timeModal) => {
  const filePath = `${message.split(".")[0]}\\${filename}`;
  console.log(filePath, timeModal);
  let command = `python ../demoCustom2.py ${filePath} ${cam} ${timeModal}`;
  return new Promise((resolve, reject) => {
    let commandTemplate = `conda run -n testEnv ${command}`;
    // const eventName = "script-result";

    exec(commandTemplate, (error, stdout, stderr) => {
      if (error) {
        return reject(error);
      }

      resolve({ message: message, filePath: filePath, maxScore: stdout });
    });
  });
};

const detectionOnVideoForImage = async (
  message,
  filename,
  cam,
  timeModel,
  videoIndex
) => {
  const filePath = `${message.split(".")[0]}\\${filename}`;
  console.log(filePath, cam, timeModel);
  let command = `python ../demoCustom4.py ${filePath} ${cam} ${videoIndex} ${timeModel}`;
  return new Promise((resolve, reject) => {
    let commandTemplate = `conda run -n testEnv ${command}`;
    // const eventName = "script-result";

    exec(commandTemplate, (error, stdout, stderr) => {
      if (error) {
        return reject(error);
      }
      console.log(stdout);
      resolve({ message: message, filePath: filePath, maxScore: stdout });
    });
  });
};

const getCameraFromFilename = (filename) => {
  console.log(filename.split("_"));
  return filename.split("_")[0]; // Assuming standard naming of files is in format ( frontGate_321312312.mp4  )
};

const callName = async (filename) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log(filename);
      resolve("Ok");
    }, 5000);
  });
};
module.exports.run_live_prediction = run_live_prediction;
module.exports.detectionOnVideo = detectionOnVideo;
module.exports.detectionOnVideoForImage = detectionOnVideoForImage;
module.exports.callName = callName;
module.exports.getCameraFromFilename = getCameraFromFilename;
