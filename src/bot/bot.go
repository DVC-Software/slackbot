package bot

import (
	"bytes"
	"encoding/json"
	"net/http"
	"os"

	"github.com/DVC-Software/slackbot/src/handlers"
	"github.com/nlopes/slack"
	"github.com/nlopes/slack/slackevents"
)

var (
	token                  string
	api                    *slack.Client
	rawUserAPIResponseData []slack.User
)

func Start() {
	slackBotConfig()
	setupEventsListeners()

}

func slackBotConfig() {
	token = os.Getenv("VERIFICATION_TOKEN")
	api = slack.New(token)
}

func setupEventsListeners() {
	http.HandleFunc("/sayhi", func(w http.ResponseWriter, r *http.Request) {
		mainBuffer := new(bytes.Buffer) 
		mainBuffer.ReadFrom(r.Body)
		requestBody := mainBuffer.String() 
		eventsAPIEvent, err := slackevents.ParseEvent(json.RawMessage{requestBody}, 
													  slackevents.OptionVerifyToken(
															  &slackevents.TokenComparator{VerificationToken: token}
													  )
													  ) 
		if err ! = nil {
			w.WriteHeader(http.StatusInternalServerError)
		}

		if eventsAPIEvent.Type == slackevents.URLVerification {
			var r *slackevents.ChallengeResponse 
			if rErr := json.Unmarshal([]byte(requestBody), &r); rErr != nil {
				w.WriteHeader(http.StatusInternalServerError)
			}
			w.Header().Set("Content-Type", "text")
			w.Write([]byte(r.Challenge))

		}
		if eventsAPIEvent.Type == slackevents.CallbackEvent {
			innerEvent := eventsAPIEvent.InnerEvent 
			switch ev := innerEvent.Data.(type) {
			case *slackevents.AppMentionEvent:
				api.PostMessage(ev.Channel, slack.MsgOptionText("heyyyy guys I just picked up that event myself ;)", false))
			}
		}
	})
	fmt.Println("Bot is actively listening for events now....")
}

