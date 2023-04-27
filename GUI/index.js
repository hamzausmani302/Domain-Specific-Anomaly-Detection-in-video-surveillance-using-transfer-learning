const express = require("express");
const app = express();

const server = require("http").createServer(app);
const io = require("socket.io")(server);
const fs = require("fs");
const path = require("path");
const { exec } = require("child_process");
const { execSync } = require("child_process");
app.set("view engine", "ejs");
// const Stream = require("node-rtsp-stream");
const router = require("./Routers/router");
const {
  run_live_prediction,
  callName,
  detectionOnVideo,
  detectionOnVideoForImage,
  getCameraFromFilename,
} = require("./serverUtils/utils");
// const BUFFER_PATH = require("./config");
const config = require("./config");
const { clearOldData } = require("./serverUtils/fileUtils");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static("./public"));

app.use(router);

io.on("connection", (socket) => {
  console.info("a new user connected");

  // socket.emit("message", "A new user connected");

  socket.on("clientMessage", (filename) => {
    //running python script on model

    //processing will be done here

    //sending processed clip back to the client

    socket.emit("showVideo", `/Files/${filename}`);
  });

  //depracated method
  socket.on("uploadEvent", (filename) => {
    const fullPath = path.resolve(__dirname, `public/Files/${filename}`);

    console.log("fullpath");
    socket.emit("showVideo", filename);
  });
  socket.on("run-script-image", async function (message, cam, timeModel) {
    //run script here
    console.log("runing script - python --version");
    console.log(cam, message, timeModel);
    //break vdeo into subvideos
    const camera = getCameraFromFilename(message);
    console.log("breaking videos & testing on " + camera);

    const result = execSync(`python ../clip_maker3.py ${message}`);
    console.log(
      "reading folder",
      `C:/Users/Asus/Work/anamoly detect/Oct2022/AnomalyDetection_CVPR18/GUI/public/Inter/${
        message.split(".")[0]
      }`
    );
    const filenames = fs.readdirSync(
      `C:/Users/Asus/Work/anamoly detect/Oct2022/AnomalyDetection_CVPR18/GUI/public/Inter/${
        message.split(".")[0]
      }`
    );
    console.log("video split done");
    clearOldData(message.split(".")[0]); // delestes old data
    //run predictiion on each video
    console.log(filenames);
    const outputs = [];
    //##########33 testing
    for (let i = 0; i < filenames.length; i++) {
      console.log(`for ${filenames[i]}`);
      const val = await detectionOnVideoForImage(
        message,
        filenames[i],
        camera,
        timeModel,
        i
      )
        .then((d) => {
          console.log("done processing on ", filenames[i]);
        })
        .catch((err) => {
          console.log(err);
        });
    }
    const outputFiles = fs.readdirSync(
      `C:/Users/Asus/Work/anamoly detect/Oct2022/AnomalyDetection_CVPR18/GUI/public/Outputs/${
        message.split(".")[0]
      }`
    );
    let max = 0;
    console.log("output", outputFiles);
    const imagesPayload = [];
    for (let i = 0; i < outputFiles.length; i++) {
      //get precition,, part of video , filename from filename and send

      const results = outputFiles[i]
        .substring(0, outputFiles[i].lastIndexOf("."))
        .split("-");
      console.log(results);
      if (results[1] && parseInt(results[1]) > max) {
        max = parseInt(results[1]);
      }
      imagesPayload.push({
        video_index: results[1],
        frameNo: results[2],
        score: results[3],
        imageURI: `/api/Files/${outputFiles[i]}?output=true&videoName=${
          message.split(".")[0]
        }\\${outputFiles[i]}`,
      });

      // socket.emit(
      //   "showImage",
      //   `/api/Files/${outputFiles[i]}?output=true&videoName=${
      //     message.split(".")[0]
      //   }\\${outputFiles[i]}`,
      //   results[3]
      // );
    }
    // console.log(imagesPayload);
    socket.emit("showImages", imagesPayload, max);
  });

  //send the video link to
  socket.on("run-script", async function (message, cam, timeModel) {
    //run script here
    console.log("runing script - python --version");
    console.log(cam, message, timeModel);
    //break vdeo into subvideos

    console.log("breaking videos");
    const result = execSync(`python ../clip_maker3.py ${message}`);
    console.log(
      "reading folder",
      `C:/Users/Asus/Work/anamoly detect/Oct2022/AnomalyDetection_CVPR18/GUI/public/Inter/${
        message.split(".")[0]
      }`
    );
    const filenames = fs.readdirSync(
      `C:/Users/Asus/Work/anamoly detect/Oct2022/AnomalyDetection_CVPR18/GUI/public/Inter/${
        message.split(".")[0]
      }`
    );
    console.log("video split done");
    clearOldData(message.split(".")[0]); // delestes old data

    //run predictiion on each video
    console.log(filenames);
    const outputs = [];
    //##########33 testing
    for (let i = 0; i < filenames.length; i++) {
      console.log(`for ${filenames[i]}`);
      const val = await detectionOnVideo(message, filenames[i], cam, timeModel)
        .then((d) => {
          console.log("done processing on ", filenames[i]);
          socket.emit(
            "showVideo",
            `/api/Files/${d.message}?output=true&videoName=${d.filePath}`
          );
        })
        .catch((err) => {
          console.log(err);
        });
    }
  });

  socket.on("run-live-detect", async (cam) => {
    console.log("starting live predictions");
    //run prediction based on camera
    let i = 2;
    while (i < 10) {
      i++;
      await run_live_prediction(cam, i)
        .then((d) => {
          const data = fs.readFileSync(config.BUFFER_PATH, "utf8");
          socket.emit("message", i.toString() + "on " + cam + data);
          socket.emit("showVideoLive", `/api/Files/output${i}.mp4`, data);
          // socket.emit(
          //   "showVideoLive",
          //   `/api/Files/output${i}.mp4?output=true&videoName=Camera/output${i}.mp4`,
          //   data
          // );
        })
        .catch((err) => {
          console.log(err);
          socket.emit("message", err.message);
        });
      console.log("done");
    }
    //send the clipped prediction back to hte client  //showVideo event triggered
  });
});

server.listen(3000, () => {
  console.log("setver started");
});
