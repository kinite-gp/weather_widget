import json

config_file = open("/home/kinite/Documents/GitHub/weather_widget/config.json", "r")
config = json.loads(config_file.read())

AREA = config["area"]
CLOSE_AFTER = config["close_after"]*1000

