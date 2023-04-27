const socket = io();

var timeModel = "day";
function handleClick() {
  console.log("starting processing for video");
  socket.emit(
    "run-script",
    document.getElementById("filename").innerText,
    model,
    timeModel
  );
}
function printmodel() {
  console.log(timeModel);
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
