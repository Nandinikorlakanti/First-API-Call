import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ Please set GEMINI_API_KEY in your .env file.")
    exit()

# Configure the Gemini API
genai.configure(api_key=API_KEY)

# Create model instance with correct version
model = genai.GenerativeModel('models/gemini-2.0-flash-lite')


# System prompt
system_prompt = "You are a helpful and concise AI assistant."

# User input
user_input = input("🧑 Enter your question: ")

# Combine system prompt with user query
full_prompt = f"{system_prompt}\n\nUser: {user_input}"

# Generate response
response = model.generate_content(full_prompt)

# Output result
print("\n🤖 Assistant's Response:\n")
print(response.text.strip())

# Print token usage if available
if hasattr(response, "usage_metadata"):
    usage = response.usage_metadata
    print("\n📊 Token Usage:")
    print(f"Prompt Tokens: {usage.prompt_token_count}")
    print(f"Response Tokens: {usage.candidates_token_count}")
    print(f"Total Tokens: {usage.total_token_count}")
else:
    print("\nℹ️ Token usage information not available.")
