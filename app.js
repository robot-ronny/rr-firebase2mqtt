var admin = require("firebase-admin");
var mqtt = require("mqtt");
var program = require("commander");
var once_recieved = false;

program
  .version('0.1.0')
  .option('-f, --firebase <url>', 'Firebase url')
  .option('-c, --cert <cert>', 'serviceAccountKey path')
  .option('-h, --host <host>', 'MQTT broker host', defaultValue="localhost")
  .option('-p, --port <port>', 'MQTT broker port', defaultValue=1883)
  .parse(process.argv);

if ((program.firebase && program.cert) == undefined) {
    console.log(" ==> Error: Enter firebase url and serviceAccountKey path")
    process.exit()
}

var client  = mqtt.connect('mqtt://{program.host}:{program.port}')
 
client.on('connect', function () {
  console.log("Connected to MQTT broker")
})

admin.initializeApp({
  credential: admin.credential.cert(program.cert),
  databaseURL: program.firebase
});

var ref = admin.database().ref("/commands/go");
ref.on("value", snapshot => {
  if (once_recieved) {
    var recieved_data = snapshot.val();
    var message = JSON.stringify({"interval": parseInt(recieved_data.value), "speed": 100});
    client.publish(`ronny/go/${recieved_data.direction}`, message);
    console.log(`Message send to MQTT broker ${message}`)
  }

  else {
    once_recieved = true;
  }
})