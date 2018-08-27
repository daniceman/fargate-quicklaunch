package main

import (
	"io"
	"log"
	"net/http"
)

const msg = `
		I AM RUNNING ON FARGATE!
`

func main() {
	log.Println("Booting..")
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/plain")
	w.WriteHeader(http.StatusOK)
	io.WriteString(w, msg)
}

