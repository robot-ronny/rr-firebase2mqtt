# rr-firebase2mqtt
Connect Firebase to MQTT for movement

## Install
1. Generate and download private key from Firebase
2. Clone repository
```
https://github.com/robot-ronny/rr-firebase2mqtt
```
3. Navigate to cloned repository
```
cd rr-firebase2mqtt
```
4. Install dependencies
```
npm install
```
5. Start script with firebase url and cert path
```
node app.js -f https://your-database.firebaseio.com -c patt/to/cert
```

## Help
```
>>> node app.js --help
Usage: app [options]

Options:
  -V, --version         output the version number
  -f, --firebase <url>  Firebase url
  -c, --cert <cert>     serviceAccountKey path
  -h, --host <host>     MQTT broker host (default: "localhost")
  -p, --port <port>     MQTT broker port (default: 1883)
  -h, --help            output usage information
```
