package main

import (
	"fmt"
	"log"
	"net/http"
	"github.com/DVC-Software/slackbot/src/bot" 
)
/**
*
* TODO
* - Implement createUser rquest
 */

func main() {
	fmt.Println("Server Root Up...")

	http.HandleFunc("/", indexHandler)

	log.Fatal(http.ListenAndServe(":8000", nil))
}

// URL Handlers
func indexHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("SETTING UP BOT")
	bot.Start()
}
