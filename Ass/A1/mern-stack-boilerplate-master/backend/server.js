const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');
const PORT = 4000;
const DB_NAME = "tutorial"
const rla = "mongodb+srv://ruchitha:Ruchi123@cluster0.mk4os.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
// routes
var testAPIRouter = require("./routes/testAPI");
var UserRouter = require("./routes/Users");

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Connection to MongoDB
/*mongoose.connect('mongodb://127.0.0.1:27017/' + DB_NAME, { useNewUrlParser: true });
const connection = mongoose.connection;
connection.once('open', function() {
    console.log("MongoDB database connection established successfully !");
})*/
DB = rla;
mongoose
  .connect(DB, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    console.log("MongoDB database connection established successfully !");
  })
  .catch((err) => {
    console.log("MongoDB database connection error !", err);
  });

// setup API endpoints
app.use("/api/testAPI", testAPIRouter);
app.use("/api/user", UserRouter);

app.listen(PORT, function() {
    console.log("Server is running on Port: " + PORT);
});
