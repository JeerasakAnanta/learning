package handlers

import (
	"encoding/json"
	"net/http"
	"go-api/models"
)

func GetUsers(w http.ResponseWriter, r *http.Request) {
	users := []models.User{
		{ID: 1, Name: "Alice"},
		{ID: 2, Name: "Bob"},
	}
	json.NewEncoder(w).Encode(users)
}
