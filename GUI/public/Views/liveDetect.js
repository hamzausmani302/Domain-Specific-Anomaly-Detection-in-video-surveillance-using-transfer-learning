console.log("script loaded");
const camera = ["frontGate", "outsideSports"];
let currentCamera = camera[0];
const selectionTemplate = `
<select id="selectbox"> 
    ${camera.map((el) => `<option ${el}> ${el}</option>`)}
</select>`;
function cameraChange(e) {
  currentCamera = e.target.value;
}
function runDetection() {
  socket.emit("run-live-detect", currentCamera);
}
document.getElementById("selector-container").innerHTML = selectionTemplate;

document.getElementById("selectbox").addEventListener("change", cameraChange);

const socket = io();

console.log("connected");

socket.on("message", (message) => {
  console.log(message);
  //   socket.emit("clientMessage", document.getElementById("filename").innerText);
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
        <h4>90%</h4>
        </div>`;
});

socket.on("showVideoLive", (url, percentage) => {
  console.log("press run script to start ", url);
  document.getElementById("video-container").innerHTML += `<div>
  
          <div>
          <video width="500" height="300" controls>
          <source src="${url}" type="video/mp4" autoplay>
        </video>
          </div>
          <h4>${percentage}</h4>
          </div>`;
});
