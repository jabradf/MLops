package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

// index handler
func indexHandler(w http.ResponseWriter, r, *http.Request) {
	if r.URL.Path != "/" {
		http.NotFound(w, r)
	}
	fmt.Fprint(w, "Hello world!")
}

func main() {
	http.HanleFunc("/", indexHandler)

	if port == "" {
		port = "8080"
		log.Printf("Defaulting to port %s", port)
	}

	log.Printf("Listening on port %s", port)
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		log.Fatal(err)
	}
}