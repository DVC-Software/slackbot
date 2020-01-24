package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	fmt.Println("Server spooling up...")

	http.HandleFunc("/", indexHandler)
	log.Fatal(http.ListenAndServe(":8000", nil))
}

// URL Handlers
func indexHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("SLACK BOT IS HERE")
}
