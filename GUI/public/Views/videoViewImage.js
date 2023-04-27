console.log("worlcome view vview image");
const socket = io();
var timeOfDay = "day";
var model = "frontgate";
function handleClick() {
  console.log("starting processing for video");
  socket.emit(
    "run-script-image",
    document.getElementById("filename").innerText,
    model,
    timeOfDay
  );
}
function printmodel() {
  console.log(timeOfDay);
}

$(document).ready(() => {
  console.log("connected");

  socket.on("message", (message) => {
    console.log(message);
    socket.emit("clientMessage", document.getElementById("filename").innerText);
  });

  socket.on("script-result", (result) => {
    console.log(result);
  });
  socket.on("showImages", (payload, videoPartCount) => {
    // console.log("imageUrl", url);
    const groupImagesByVideo = (images) => {
      let groupedImages = {};
      for (let i = 0; i <= videoPartCount; i++) {
        groupedImages[i] = [];
      }
      console.log("inital", groupedImages);
      for (let image of images) {
        groupedImages[parseInt(image.video_index)].push(image);
      }
      return groupedImages;
    };

    const grouped = groupImagesByVideo(payload);
    console.log(grouped);
    for (const key in Object.keys(grouped)) {
      console.log(typeof key);
      document.getElementById("video-flex").innerHTML += `<div>
      <h4>Time Duration : ${parseInt(key) * 30} - ${
        (parseInt(key) + 1) * 30
      }</h4></div>`;
      // display: flex;flex-direction: row;flex-wrap: wrap;
      document.getElementById(
        "video-flex"
      ).innerHTML += `<div id="video-row-container-${key}" style="display: flex;flex-direction: row;flex-wrap: wrap;">
      </div>`;
      if (grouped[key].length == 0) {
        document.getElementById(`video-row-container-${key}`).innerHTML +=
          "No anomaly found";
      }
      for (let image of grouped[key]) {
        document.getElementById(
          `video-row-container-${key}`
        ).innerHTML += `<div style="display:flex;flex-direction:column;flex-wrap:wrap;justify-content:between;margin:10px;">
          <a target="_blank" href="${image.imageURI}">
          <div>
          <img style="width:150px;height:150px" src=${image.imageURI}/>
      </div>
      </a>
          <div>
              <p style="text-align:center;">${image.score}</p>
          </div>
          </div>`;
      }
    }
  });

  socket.on("showVideo", (url) => {
    console.log("press run script to start ", url);
    document.getElementById("video-container").innerHTML += `<div>
    
    <div>
    <video width="500" height="300" controls>
    <source src="${url}" type="video/mp4" autoplay>
  </video>
    </div> 
    <h4>Inference from the given video</h4>
    </div>`;
  });
});
