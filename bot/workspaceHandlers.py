import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi
import json

import jsonModels

app = Flask(__name__)
SLACK_EVENTS_ADAPTER = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'],
                                         '/slack/events', app)
SLACK_WEB_CLIENT = WebClient(token=os.environ['VERIFICATION_TOKEN'])


class Hireout:
    def __init__(self,
                 channel,
                 hireoutTitleText,
                 when,
                 package,
                 djs='na',
                 theme='na',
                 notes='na'):
        self.channel = channel
        self.hireoutTitleText = hireoutTitleText
        self.when = when
        self.package = package
        self.djs = djs
        self.theme = theme
        self.notes = notes

        # main json body that'll encapsulate the data
        self.hireout_created_message = {
            "blocks": [],
        }
    def sendHireoutMessage(self):
        self._buildMessageJSON()
        finalData = json.dumps(self.hireout_created_message, sort_keys=True, indent=4)
        return finalData

    def djSignup(self):
        pass

    def _buildMessageJSON(self):
        self.hireout_created_message["blocks"].append(
            jsonModels.makeNotifTitleBlock(self.hireoutTitleText)
        )
        self.hireout_created_message["blocks"].append(
            jsonModels.makeNotifBodyBlock(self.theme,
                                          self.when,
                                          self.notes,
                                          self.package,
                                          self.djs
            )
        )
        self.hireout_created_message["blocks"].append(
            jsonModels.makeActionBlocks()
        )

class OfficeEquipmentTracker:
    def __init__(self, hireout, times):
        self.hireout = hireout
        self.times = times

    def listAllOfficeEquipment(self):
        pass

    @staticmethod
    def buildMessageJSON(self):
        parentBlock = {
            "blocks": [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "A hireout has been created!"
                }
            }]
        }

        return parentBlock
