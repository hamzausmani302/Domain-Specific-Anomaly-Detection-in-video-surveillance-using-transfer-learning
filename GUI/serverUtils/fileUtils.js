const path = require("path");
const fs = require("fs");
const checkFolderExists = (folderPath) => {
  return fs.existsSync(folderPath);
};
const deleteFolder = (folderPath) => {
  fs.rmSync(folderPath, { recursive: true, force: true });
};
const deleteOldData = (folderName) => {
  const outputFolder = path.join(
    path.join(__dirname, "../public/Outputs"),
    folderName
  );
  if (checkFolderExists(outputFolder)) {
    deleteFolder(outputFolder);
  }
};

module.exports.clearOldData = deleteOldData;
