const { app, BrowserWindow } = require("electron");

const SIZE = {
  x: 695,
  y: 495,
};

app.on("ready", () => {
  const win = new BrowserWindow({
    minWidth: SIZE.x,
    minHeight: SIZE.y,
    webPreferences: {
      devTools: true,
      nodeIntegration: true
    }
  });
  win.removeMenu();
  win.webContents.on("dom-ready", () => {
    win.webContents.openDevTools();
  });
  win.loadURL(`file://${__dirname}/build/pages/index.html`);
});