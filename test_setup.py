
from google.colab import userdata
from google import genai

client = genai.Client(api_key=userdata.get('gemini'))

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Say 'setup working' and nothing else."
)
print(response.text)
