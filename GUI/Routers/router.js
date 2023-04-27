const express = require("express");
const router = express.Router();
const path = require("path");
var formidable = require("formidable");
var mv = require("mv");
const fs = require("fs");

router.get("/home", (req, res) => {
  res.render(path.resolve(__dirname, "../public/Views/home.ejs"));
});
router.get("/detectlive", (req, res) => {
  res.render(path.resolve(__dirname, "../public/Views/liveFeed.ejs"));
});

router.get("/", (req, res) => {
  res.render(path.resolve(__dirname, "../public/Views/index.ejs"));
});

router.post("/fileupload", (req, res) => {
  //req.setTimeout(300000);
  const form = new formidable.IncomingForm();
  form.parse(req, (err, fields, files) => {
    // console.log(fields, files);
    const returnResult = fields["result-type"];

    console.log(returnResult);
    const tempPath = files.uploadfile.filepath;
    const newPath = path.resolve(
      __dirname,
      `../public/Files/${files.uploadfile.originalFilename}`
    );
    fs.rename(tempPath, newPath, function (err) {
      if (err) throw err;
      //return res.send("File upload successful");

      //processing to be done here

      res.render(
        path.resolve(
          __dirname,
          `../public/Views/${
            returnResult === "image" ? "videoViewImage.ejs" : "videoView.ejs"
          }`
        ),
        {
          message: files.uploadfile.originalFilename,
          code: ``,
        }
      );
    });
  });
});

router.get("/conn1.js", (req, res) => {
  res.sendFile(path.resolve(__dirname, "../public/Views/conn1.js"));
});
router.get("/liveDetect.js", (req, res) => {
  res.sendFile(path.resolve(__dirname, "../public/Views/liveDetect.js"));
});

router.get("/videoViewImage.js", (req, res) => {
  res.sendFile(path.resolve(__dirname, "../public/Views/videoViewImage.js"));
});

router.get("/api/Files/:filename", (req, res) => {
  console.log("test");
  const { filename } = req.params;
  const { output } = req.query;
  const { videoName } = req.query;

  console.log(filename);
  console.log("video", videoName);

  if (!output) {
    res.sendFile(path.resolve(__dirname, `../public/Files/${filename}`));
  } else {
    res.sendFile(path.resolve(__dirname, `../public/Outputs/${videoName}`));
  }
  // res.render(path.resolve(__dirname , "../public/Views/videoView.ejs"))
});
module.exports = router;
