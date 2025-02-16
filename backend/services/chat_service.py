import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key")

def chat_response(user_message, conversation_history=None):
    if conversation_history is None:
        conversation_history = []
    
    # System message defining the HR agent's role and behavior
    system_message = {
        "role": "system",
        "content": """
            You are an experienced HR assistant specializing in recruitment outreach. 
            Help HR professionals craft effective recruiting strategies and messages by:
            - Asking relevant questions about their target candidates, role requirements, and company culture
            - Providing guidance on best practices for recruitment outreach
            - Suggesting improvements to their messaging approach
            - Maintaining a professional and supportive tone
            Be proactive in gathering necessary information and offering specific, actionable advice.
        """
    }
    
    # Construct the messages array with system prompt and conversation history
    messages = [system_message] + conversation_history + [
        {"role": "user", "content": user_message}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7  # Add some creativity while keeping responses professional
    )
    
    # Return both the response and the updated conversation history
    assistant_response = response["choices"][0]["message"]["content"]
    conversation_history.append({"role": "user", "content": user_message})
    conversation_history.append({"role": "assistant", "content": assistant_response})
    
    return assistant_response, conversation_history
