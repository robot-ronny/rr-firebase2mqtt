import sys
import click
import json
import paho.mqtt.client as mqtt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


@click.command()
@click.option("-c", "--config-file", help="Firebase config file path", required=True, type=click.Path(exists=True))
@click.option("-u", "--firebase-url", help="Firebase url", required=True)
@click.option("-h", "--host", help="MQTT hostname", default="localhost")
@click.option("-p", "--port", help="MQTT port", default=1883)
def cli(config_file=None, firebase_url=None, host=None, port=None):
    def on_connect(client, userdata, flags, rc):
        print("MQTT: Connected")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host, port, 60)
    client.loop_start()

    cred = credentials.Certificate(config_file)
    firebase_admin.initialize_app(cred, {'databaseURL': firebase_url})
    ref = db.reference("/")

    def callback(msg):
        data = msg.data
        if str(msg.path).startswith("/commands/go/"):
            print(data)
            client.publish("ronny/go/{0}".format(data))

    ref.listen(callback)

def main():
    try:
        cli()
    except Exception as e:
        click.echo("Exited with error: {0}".format(e))
        sys.exit(1)
    except KeyboardInterrupt:
        pass