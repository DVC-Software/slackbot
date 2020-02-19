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
    '''
    @args:
      - Hireout reference
      - state: list that contains
        [at hireout, in maitnence, in office, sell it]
        can only be in one state at a time
        NOTE: would be better represented in an Enum... refractor later
      - gearName: ie "Pioneer CDJ Nexus 2"...
      - description: any other misc notes about the gear
    '''
    def __init__(self, hireout, state, gearName, description):
        self.hireout = hireout
        self.state = state
        self.gearName = gearName
        self.description = description

        # make api call to golang server to grab all current gear in office
        self.allGear = []

        # final json to send to slack
        self.listAllGearJSON = []

        # Set channel to whatever hireout it attaches itself to
        self.channel = hireout.channel

    def listAllOfficeEquipment(self):
        pass

    def sendMessageJSON(self):
        self._buildGearJSON()
        finalData = json.dumps(self.listAllGearJSON,
                               sort_keys=True,
                               indent=4
        )
        SLACK_WEB_CLIENT.chat_postMessage(channel=self.channel,
                                         blocks=finalData
        )

    def _buildGearJSON(self):
        # title
        self.listAllGearJSON.append(
            jsonModels.makeNotifTitleBlock("All current gear in the office")
        )
        self.listAllGearJSON.append(jsonModels.makeSpacer())

        # Gear list with dropdown menu to change its state
        self.listAllGearJSON.append(
            jsonModels.makeDropDownMenu(self.gearName)
        )
        self.listAllGearJSON.append(jsonModels.makeSpacer())


