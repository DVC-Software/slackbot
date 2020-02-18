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
        self.hireout_created_message = []


    def sendStaticHireoutMessage(self):
        self._buildStaticMessageJSON()
        finalData = json.dumps(self.hireout_created_message, sort_keys=True, indent=4)
        SLACK_WEB_CLIENT.chat_postMessage(channel=self.channel,
                                          blocks=finalData
        )
        #return finalData

    def djSignup(self):
        pass

    def _buildStaticMessageJSON(self):
        self.hireout_created_message.append(
            jsonModels.makeNotifTitleBlock(self.hireoutTitleText)
        )
        self.hireout_created_message.append(
            jsonModels.makeNotifBodyBlock(self.theme,
                                          self.when,
                                          self.notes,
                                          self.package,
                                          self.djs
            )
        )
        self.hireout_created_message.append(
            jsonModels.makeActionBlocks()
        )

    def sendHireoutSignupMessage(self):
        self._buildDynamicMessageJSON()
        finalData = json.dumps(self.hireout_created_message,
                               sort_keys=True,
                               indent=4
        )
        SLACK_WEB_CLIENT.chat_postMessage(channel=self.channel,
                                          blocks=finalData
        )


    def _buildDynamicMessageJSON(self):
        self.hireout_created_message.append(
            jsonModels.makeNotifTitleBlock(self.hireoutTitleText)
        )
        self.hireout_created_message.append(
            jsonModels.makeSpacer()
        )
        self.hireout_created_message.append(
            jsonModels.makeNotifBodyBlock(
                self.theme,
                self.when,
                self.notes,
                self.package,
                self.djs
            )
        )
        self.hireout_created_message.append(
            jsonModels.makeSpacer()
        )
        # Sign up for dj time slots
        self.hireout_created_message.append(
            jsonModels.makeNotifTitleBlock("*Sign up for a time to spin!*")
        )
        self.hireout_created_message.append(
            jsonModels.makeSpacer()
        )
        self.hireout_created_message.append(
            jsonModels.makeSignupSection("4-6pm")
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
