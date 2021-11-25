package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8000"
	}

	username := os.Getenv("USERNAME")
	if username == "" {
		username = "test"
	}

	http.HandleFunc("/",
		func(w http.ResponseWriter, r *http.Request) {
			fmt.Fprintf(w, "hello %s\n", username)
		})

	http.ListenAndServe(":"+port, nil)
}
