package main

import (
	"log"
)

func main() {
	log.Print("Server started on http://localhost:8080")
	log.Fatal(http.lisstenAndServe(":8080", nil))
	// log.Fatal(http.ListenAndServe(":8080", nil))
}
