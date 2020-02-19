

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

def makeTextBlock(text):
    text_body_block = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": text
        }
    }

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


# Static select dropdown menu
def makeDropDownMenu(gearText):
    actions = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": gearText,
        },
        "accessory": {
            "type": "static_select",
            "placeholder": {
                "type": "plain_text",
                "text": "Manage Gear"
            },
            "options": [
                {
                    "text": {
                        "type": "plain_text",
                        "text": "DEFAULT_TEXT"
                    },
                    "value": "value-0"
                }
            ]
        }
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
