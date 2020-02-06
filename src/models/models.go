package models

type DVCProfile struct {
	// the following fields will be directly from slack api response
	FirstName   string `json:"firstName"`
	LastName    string `json:"lastName"`
	DisplayName string `json:"displayName"`
	Email       string `json:"email"`

	// the rest are DVC Specific...
	IsVerified bool `json:"isVerified"`

	// only 3 options for training status:
	// Group Training, One on one training, or training completed
	TrainingStatus string `json:"trainingStatus"`

	// president, treasurer, dj trainer, etc....
	OrgPosition OrganizationPosition `json:"orgPosition"`
}

type OrganizationPosition struct {
	RoleName string      `json:"roleName"`
	Profile  *DVCProfile `json:"profile"`
}

type Members struct {
	SlackUserName   string      `json:"slackUserName"`
	DiscordUsername string      `json:"discordUserName"`
	IsStaff         bool        `json:"isStaff"`
	Profile         *DVCProfile `json:"profile"`
}
