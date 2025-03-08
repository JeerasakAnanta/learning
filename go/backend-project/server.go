package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	// Register the handler function for the root URL path
	http.HandleFunc("/", handler)

	// Print a message to indicate the server is starting
	fmt.Println("Listening on port http://localhost:8000")

	// Start the HTTP server on port 8000 and log any fatal errors
	log.Fatal(http.ListenAndServe(":8000", nil))
}

// handler is an HTTP handler function that writes a greeting message.
func handler(w http.ResponseWriter, r *http.Request) {
	// Write "Hello world!" to the response writer
	fmt.Fprint(w, "Hello world!")
}
