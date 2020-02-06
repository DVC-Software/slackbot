package bot

import (
	"encoding/json"
	"fmt"

	"github.com/DVC-Software/slackbot/src/models"
)

var (
	dvcUserData models.DVCProfile
)

func GetAllSlackUsers() {
	rawUserAPIResponseData, err := api.GetUsers()
	if err != nil {
		fmt.Println("Error At: ", err)
		panic("Bad API Request")
	}
	marshalledAPIResponse, err := json.Marshal(rawUserAPIResponseData)
	if err != nil {
		fmt.Println("Error marshaling raw api data: ", err)
		return
	}

	unmarshallError := json.Unmarshal(marshalledAPIResponse, &dvcUserData)
	if unmarshallError != nil {
		fmt.Println("Error unmarshalling: ", err)
		return
	}
	fmt.Println(dvcUserData)
}
