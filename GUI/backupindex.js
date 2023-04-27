const express = require("express");
const app = express();

const server = require("http").createServer(app);
const io = require("socket.io")(server);
const fs = require("fs");
const path = require("path");
const { exec } = require("child_process");
const { execSync } = require("child_process");
app.set("view engine", "ejs");

const router = require("./Routers/router");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static("./public"));

app.use(router);

io.on("connection", (socket) => {
  console.info("a new user connected");

  socket.emit("message", "A new user connected");

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

  //send the video link to
  socket.on("run-script", (message, cam) => {
    //run script here
    console.log("runing script - python --version");
    console.log(cam, message);
    //break vdeo into subvideos

    console.log("breaking videos");
    const result = execSync(`python ../clip_maker3.py ${message}`);

    const filenames = fs.readdirSync(
      `C:/Users/Asus/Work/anamoly detect/Oct2022/AnomalyDetection_CVPR18/GUI/public/Inter/${
        message.split(".")[0]
      }`
    );
    console.log("video split done");
    //run predictiion on each video
    console.log(filenames);
    for (let i = 0; i < filenames.length; i++) {
      const filePath = `${message.split(".")[0]}\\${filenames[i]}`;
      console.log(filePath);
      let command = `python ../demoCustom2.py ${filePath} ${cam}`;

      // // ////////

      let commandTemplate = `conda run -n testEnv ${command}`;
      eventName = "script-result";
      exec(commandTemplate, (error, stdout, stderr) => {
        if (error) {
          console.log("error1");
          socket.emit(eventName, error.message);
          return;
        }
        console.log("done");
        socket.emit(
          "showVideo",
          `/api/Files/${message}?output=true&videoName=${filePath}`
        );
      });
    }
    //command execution
  });
});

server.listen(3000, () => {
  console.log("setver started");
});
