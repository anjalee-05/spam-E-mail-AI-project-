import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class AIAssistant:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.is_ready = False
        
        if self.api_key and self.api_key != "your_api_key_here":
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-2.5-flash')
                self.is_ready = True
            except Exception as e:
                print(f"Error configuring Gemini: {e}")
                
    def generate_response(self, query, context=""):
        if not self.is_ready:
            return "⚠️ **API Key Missing**: Please add your Google Gemini API key to the `.env` file to use the AI Assistant."
            
        try:
            prompt = f"""
You are a smart, helpful AI assistant built into 'MailGuard', an email intelligence application.
You help users analyze their emails, summarize content, detect threats (spam, phishing), and answer general questions about their inbox and the overall website statistics.

Here is the data and information about the website, including overall statistics and the user's recent email context (JSON format):
{context}

User's Query: {query}

Please provide a concise, helpful, and beautifully formatted response using Markdown.
"""
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"AI Assistant Error: {e}")
            return "⚠️ Sorry, I encountered an error while processing your request. Please try again later."
