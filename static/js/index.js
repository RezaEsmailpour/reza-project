const EventEmitter = require("events");

const http = require("http");

const myEmitter = new EventEmitter();

myEmitter.on("newSale", () => {
    console.log("There was a new sale!");
});

myEmitter.on("newSale", () => {
    console.log("costumer name: ahmad");
});

myEmitter.on("newSale", data =>{
    console.log(`there are now ${data} items left in stock.`)
})

myEmitter.emit("newSale", 10);

const server = http.createServer();

server.on("request", (res, rea) => {
    console.log("requset received!");
    console.log(res.url);
    rea.end("request received");
});

server.on("request", (res, rea) => {
    console.log("another server");
});

server.listen(8000, "127.0.0.1", () => {
    console.log("waiting for request...");
});




