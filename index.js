const { app, BrowserWindow, Tray, ipcMain } = require("electron");
const path = require("path");

let tray;


ipcMain.on('reloadpls', (event, arg) => {

})

const SIZE = {
  x: 695,
  y: 495,
};

app.on("ready", () => {
  tray = new Tray('./ico.ico');
  const win = new BrowserWindow({
    minWidth: SIZE.x,
    minHeight: SIZE.y,
    frame:false,
    icon:'./ico.ico',
    webPreferences: {
      devTools: true,
      nodeIntegration: true,
      contextIsolation: false
    }
  });
  win.webContents.on("dom-ready", () => {
    win.webContents.openDevTools();
    win.removeMenu();
  });
  win.loadURL(`file://${__dirname}/build/pages/index.html`);
  
  tray.on('click', function(e){
    if (win.isVisible()) {
      win.hide();
    } else {
      win.show();
    }
  });


});