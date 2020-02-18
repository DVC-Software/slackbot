

# (1) new hireout notification
def makeNotifTitleBlock(titleText):
    notification_title_block = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": titleText
            }
    }
    return notification_title_block


def makeNotifBodyBlock(theme, time, notes, package, djs):
    notification_body_block = {
            "type":
            "section",
            "fields": [{
                "type": "mrkdwn",
                "text": "*Theme:*\n" + theme
            }, {
                "type": "mrkdwn",
                "text": "*When:*\n" + time
            }, {
                "type": "mrkdwn",
                "text": "*Notes:*\n" + notes
            }, {
                "type": "mrkdwn",
                "text": "*Package:*\n" + package
            }, {
                "type": "mrkdwn",
                "text": "*DJs:*\n" + djs
            }]
    }
    return notification_body_block


# TODO Need to hook this up to api call to golang server
def makeEditButton(style="primary"):
    edit_button_block = {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Edit"
                    },
                    "style": style,
                    "value": "click_me_123"
    }
    return edit_button_block


def makeActionBlocks():
    actions = {
            "type":
            "actions",
            "elements": [
                makeEditButton()
            ],
    }
    return actions


def makeSignupSection(djSetTime=""):
    signupArea = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*{}*".format(djSetTime)
        },
        "accessory": {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "Choose"
            },
            "value": "click_me_123"
        }
    }
    return signupArea


def makeSpacer():
    divider = {
        "type": "divider"
    }
    return divider


def insertImageHorizontally(img_url):
    image = {
        "type": "image",
        "image_url": img_url,
        "alt_text": "calendar image link"
    }
    return image

# (2) hireout dj sign up form


HIREOUT_SIGNUP_FORM = {
    "blocks": [
    {
        "type": "section",
        "text": {
            "type": "plain_text",
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
            "image_url":
            "https://api.slack.com/img/blocks/bkb_template_images/notifications.png",
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
    }]
}

# (3) list all current office equipment
OFFICE_EQUIPMENT_LIST = {
    "blocks": [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":mag: List of all current office equipment"
        }
    }, {
        "type": "divider"
    }, {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*<fakeLink.toYourApp.com|CDJ Roadcase (x8)>*\ncdj cases"
        },
        "accessory": {
            "type":
            "static_select",
            "placeholder": {
                "type": "plain_text",
                "text": "Manage"
            },
            "options": [{
                "text": {
                    "type": "plain_text",
                    "text": "At hireout"
                },
                "value": "value-0"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "Sell it"
                },
                "value": "value-1"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "In Maitnence"
                },
                "value": "value-2"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "In Office"
                },
                "value": "value-3"
            }]
        }
    }, {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text":
            "*<fakeLink.toYourApp.com|Pioneer CDJs (x2)>*\ncdj nexux 2000"
        },
        "accessory": {
            "type":
            "static_select",
            "placeholder": {
                "type": "plain_text",
                "text": "Manage"
            },
            "options": [{
                "text": {
                    "type": "plain_text",
                    "text": "At hireout"
                },
                "value": "value-0"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "Sell it"
                },
                "value": "value-1"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "In Maitnence"
                },
                "value": "value-2"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "In Office"
                },
                "value": "value-3"
            }]
        }
    }, {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text":
            "*<fakeLink.toYourApp.com|Poneer DJM Nexux 2>*\nPioneer mixer"
        },
        "accessory": {
            "type":
            "static_select",
            "placeholder": {
                "type": "plain_text",
                "text": "Manage"
            },
            "options": [{
                "text": {
                    "type": "plain_text",
                    "text": "At hireout"
                },
                "value": "value-0"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "Sell it"
                },
                "value": "value-1"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "In Maitnence"
                },
                "value": "value-2"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "In Office"
                },
                "value": "value-3"
            }]
        }
    }, {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text":
            "*<fakeLink.toYourApp.com|Uplight kit>*\npack of 4 uplights"
        },
        "accessory": {
            "type":
            "static_select",
            "placeholder": {
                "type": "plain_text",
                "text": "Manage"
            },
            "options": [{
                "text": {
                    "type": "plain_text",
                    "text": "At hireout"
                },
                "value": "value-0"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "Sell it"
                },
                "value": "value-1"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "In Maitnence"
                },
                "value": "value-2"
            }, {
                "text": {
                    "type": "plain_text",
                    "text": "In Office"
                },
                "value": "value-3"
            }]
        }
    }, {
        "type": "divider"
    }, {
        "type":
        "actions",
        "elements": [{
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "Next 5 Results"
            },
            "value": "click_me_123"
        }]
    }]
}
