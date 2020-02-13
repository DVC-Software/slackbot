import slack
import requests
import json
import os

# TODO load this from .env docker file
client = slack.WebClient(os.environ['VERIFICATION_TOKEN'])
API_DEV_ENDPOINT = 'http://0.0.0.0:8080'
HEADERS = {'Content-Type': 'application/json'}


'''Member will hold all data needed for full member creation
Note that this will also include Discord ID as well
     but for now it will be left blank?
'''
class Member:
    def __init__(self, slackID, slackName, discordID=''):
        self.slackID = slackID
        self.slackName = slackName
        self.discordID = discordID

    def toJSON(self):
        dvcMemberStruct = {
            'Name': self.slackName,
            'SlackUserID': self.slackID,
            'DiscordUserID': '',
            'CreatedFrom': '',
        }
        jsonData = json.dumps(dvcMemberStruct)
        return jsonData


def postChatMessage(message):
    client.chat_postMessage(channel='CT1R99NER',
                            text=message)

# Gets master json response of all users in slack workspace
def getAllSlackUsers():
    members = client.users_list()
    return members['members']

def getSlackUserIDs():
    slackUsers = getAllSlackUsers()
    slackIDs = set()
    for id in slackUsers:
        slackIDs.add(id['id'])
    return slackIDs

def getSlackUserNames():
    slackUsers = getAllSlackUsers()
    slackFullNames = set()
    for name in slackUsers:
        slackFullNames.add(name['name'])
    return slackFullNames

# Will send relevant data to create member in backend dvc api
# also note that discord data will be left empty for now
def sendNamesToDVC_API():
    #slackUserIDs = getSlackUserIDs()
    slackUserNames = getSlackUserNames()

    #for user_id in slackUserIDs:
    #    for name in slackUserNames:
    #        dvcMember = Member(user_id, name)
    #       memberJSON = json.dumps(dvcMember.toJSON())
    #        apiReq = requests.post(API_DEV_ENDPOINT + '/member/create',
    #                               data=memberJSON,
    #                               headers=HEADERS)
    #        print(apiReq.text)
    #apiReq = requests.get(API_DEV_ENDPOINT + '/name/show')
    jsonData = {'name': 'hennyg#'}
    apiReq = requests.post(API_DEV_ENDPOINT + '/name/create',
                           data=jsonData,
                           headers=HEADERS)
    print(apiReq.text)
    print(slackUserNames)


if __name__ == "__main__":
    sendNamesToDVC_API()

