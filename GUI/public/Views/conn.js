

const socket = io();


function handleClick(){

    socket.emit("run-script" , "running python script");

}

socket.on("message" , (message)=>{
    console.log(message);

})

socket.on("showVideo" , (url)=>{
    console.log("ru",url)
    document.getElementById("video-container").innerHTML += `<video width="320" height="240" controls>
    <source src="${url}" type="video/mp4">
  </video>`

})
document.getElementById("file-input")
.addEventListener("change" , (event)=>{
    console.log(event.target.value);    

})

document.getElementById("file-form")
.addEventListener("submit" , (event)=>{
    console.log("file submitted - front end");
    const filename = $("#file-input").val();
    const fileParts =filename.split("\\");
    const len = fileParts.length;

    socket.emit("uploadEvent"  ,fileParts[len-1] );

})