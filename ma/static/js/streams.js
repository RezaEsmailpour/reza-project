const fs = require('fs');
const server = require('http').createServer();

server.on('request', (req, res) => {
    // Solution 1
    // fs.readFile('../index.html', (rr, das) => {
    //     if(rr) console.log(rr);
    //     res.end(das);
    // });

    // Soluiton 2
    // const readable = fs.createReadStream("text1.txt");
    // readable.on("data", chunk => {
    //     res.write(chunk);
    // });
    // readable.on("end", () => {
    //     res.end();
    // });

    //Solution 3
    const readable = fs.createReadStream("text.txt");
    readable.pipe(res);
});

server.listen(8000, "127.0.0.1", () => {
    console.log("listening...");
});