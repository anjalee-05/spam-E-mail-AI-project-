import os
from ai_service import AIAssistant
from dotenv import load_dotenv

load_dotenv()

assistant = AIAssistant()
print(f"Is ready? {assistant.is_ready}")
if assistant.is_ready:
    print("Testing generate_response...")
    response = assistant.generate_response("hello", "[]")
    print(response)
else:
    print("Assistant not ready. API Key missing or invalid.")
