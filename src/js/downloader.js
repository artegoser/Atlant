const fs = require("fs");
const fetch = require("node-fetch");
class Downloader{
    async downloadHttp(url,path) {
        const res = await fetch(url);
        let bytes = res.headers.get('content-length');
        const fileStream = fs.createWriteStream(path);
        let bytescheck = setInterval(()=>{
            this.percent = (fileStream.bytesWritten/bytes)*100;
        }, 0);
        await new Promise((resolve, reject) => {
            res.body.pipe(fileStream);
            res.body.on("error", reject);
            fileStream.on("finish", ()=>{
                this.percent = (fileStream.bytesWritten/bytes)*100;
                clearInterval(bytescheck);
                resolve(this.percent);
            });
        });
    }
}
module.exports = Downloader;