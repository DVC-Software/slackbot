import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi

app = Flask(__name__)
slackEventsAdapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'],
                                       '/slack/events',
                                       app)
slackWebClient = WebClient(token=os.environ['VERIFICATION_TOKEN'])

class Hireout:


    def __init__(self, channel,
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

        MODAL_TEMPLATE = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": self.hireoutTitleText
                    }
                },

                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": "*Theme:*\n" + self.theme
                        },

                        {
                            "type": "mrkdwn",
                            "text": "*When:*\n" + self.when
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Notes:*\n" + self.notes
                        },

                        {
                            "type": "mrkdwn",
                            "text": "*Package:*\n" + self.package
                        },

                        {
                            "type": "mrkdwn",
                            "text": "*DJs:*\n" + self.djs
                        }
                    ]  # end modal body fields
                },

                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text":  {
						    "type": "plain_text",
						    "emoji": "true",
					        "text": "Edit"
					    },
				        "style": "primary",
					    "value": "click_me_123"
                        },  # end edit button
                    ],
                },   # end actions list
            ],  # end template namespace def
        }

    def sendHireoutMessage(self):
        pass

    def djSignup(self):
        pass



class OfficeEquipmentTracker:

    def __init__(self):
        pass

    def listAllOfficeEquipment(self):
        pass



# (1) Hireout creation event created message
'''
{
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "A new hireout has been created."
			}
		},
		{
			"type": "section",
			"fields": [
				{type": "mrkdwn",
					"text": "*Theme:*\nEDM music"
				},
				{
					"type": "mrkdwn",
					"text": "*When:*\nMay 10"
				},
				{
					"type": "mrkdwn",
					"text": "*Notes:*\nSet up dj booth near the bar"
				},
				{
					"type": "mrkdwn",
					"text": "*Package:*\n xdj, uplights, microphone"
				},
				{
					"type": "mrkdwn",
					"text": "*DJs:*\n staff1, staff2..."
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": true,
						"text": "Edit"
					},
					"style": "primary",
					"value": "click_me_123"
				}
			]
		}
	]
}
'''

# (2) Hireout event created but staff members select time to spin
'''
{
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"emoji": true,
				"text": "A hireout has been created!"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Sun God 2020\nSaturday, April 27, 4-6pm\nRIMAC"
			},
			"accessory": {
				"type": "image",
				"image_url": "https://api.slack.com/img/blocks/bkb_template_images/notifications.png",
				"alt_text": "calendar thumbnail"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Sign up for a time to spin!*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*4:00-4:30pm*\n@Staffmember1"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"emoji": true,
					"text": "Choose"
				},
				"value": "click_me_123"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*4:30-5:00pm*\n@Staffmember2"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"emoji": true,
					"text": "Choose"
				},
				"value": "click_me_123"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*5:00-6:00pm*\n @Staffmember4, ~@Staffmember3~"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"emoji": true,
					"text": "Choose"
				},
				"value": "click_me_123"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*<fakelink.ToMoreTimes.com|Show more times>*"
			}
		}
	]
}
'''

# List all office eqpt in office
'''
{
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":mag: List of all current office equipment"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*<fakeLink.toYourApp.com|CDJ Roadcase (x8)>*\ncdj cases"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"emoji": true,
					"text": "Manage"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "At hireout"
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "Sell it"
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "In Maitnence"
						},
						"value": "value-2"
					},
                    {
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "In Office"
						},
						"value": "value-3"
					}
				]
			}
		},
		
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*<fakeLink.toYourApp.com|Pioneer CDJs (x2)>*\ncdj nexux 2000"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"emoji": true,
					"text": "Manage"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "At hireout"
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "Sell it"
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "In Maitnence"
						},
						"value": "value-2"
					},
                    {
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "In Office"
						},
						"value": "value-3"
					}
				]
			}
		},
           
            {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*<fakeLink.toYourApp.com|Poneer DJM Nexux 2>*\nPioneer mixer"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"emoji": true,
					"text": "Manage"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "At hireout"
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "Sell it"
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "In Maitnence"
						},
						"value": "value-2"
					},
                    {
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "In Office"
						},
						"value": "value-3"
					}
				]
			}
		},
            
            {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*<fakeLink.toYourApp.com|Uplight kit>*\npack of 4 uplights"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"emoji": true,
					"text": "Manage"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "At hireout"
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "Sell it"
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "In Maitnence"
						},
						"value": "value-2"
					},
                    {
						"text": {
							"type": "plain_text",
							"emoji": true,
							"text": "In Office"
						},
						"value": "value-3"
					}
				]
			}
		},
		
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": true,
						"text": "Next 5 Results"
					},
					"value": "click_me_123"
				}
			]
		}
	]
}
'''

