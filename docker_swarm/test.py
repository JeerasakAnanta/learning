import requests

# Define the API endpoint
api_url = "http://localhost:3000/"

try:
    # Send a GET request
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Response from server:")
        print(response.text)  # Print the response content
    else:
        print(f"Error: Received status code {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")