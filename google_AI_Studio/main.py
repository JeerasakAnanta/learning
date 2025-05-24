import os

from google import genai
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# Initialize the GenAI client with your API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


# Generate content using the Gemini model
def ai_chat(user_input):
    """
    Function to generate AI chat response.
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_input,
    )

    return response.text


while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break

    # Generate and display the AI response
    ai_response = ai_chat(user_input)
    print(f"AI: {ai_response}")
