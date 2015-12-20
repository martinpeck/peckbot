from slacker import Slacker
import yaml

config = yaml.load(file('rtmbot.conf', 'r'))
api_token = config["SLACK_TOKEN"]
slack = Slacker(api_token)

# Send a message to #general channel
slack.chat.post_message('#bot_test', 'Hello fellow slackers!', as_user=True)

# Upload a file
slack.files.upload('carrot.png', channels="#bot_test")
