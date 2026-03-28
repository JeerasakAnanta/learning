# This script uses the Google GenAI client to generate content using the Gemini model. 
- code call  genai google 
  
```python
# Google GenAI Python Client
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```
