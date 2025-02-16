import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_response(user_message, conversation_history=None):
    if conversation_history is None:
        conversation_history = []
    
    print(conversation_history)

    # System message defining the HR agent's role and behavior
    system_message = {
        "role": "developer",
        "content": """
            You are an experienced HR assistant specializing in recruitment outreach. 
            Your goal is to help HR professionals craft effective, high-converting outreach strategies by:
            1️ **Understanding the Hiring Need**  
            - Ask relevant questions about the target candidates, role requirements, and company culture.  
            - Ensure clarity on job responsibilities, seniority level, and must-have qualifications.  
            - Gather information **before generating** any outreach sequence.  

            2️ **Guiding Best Practices**  
            - Provide insights on **tone, personalization, and structure** of outreach messages.  
            - Recommend **multi-step sequences** with logical progression (e.g., Intro → Value → Call-to-Action).  
            - Ensure messages are engaging and **aligned with company culture**.  

            3️ **Enhancing Outreach Messages**  
            - Suggest improvements to **wording, subject lines, and personalization tokens**.  
            - Ensure clarity, **avoid generic language**, and focus on impact-driven messaging.  

            4️ **Deciding AI Actions (Function Calling)**  
            - If the user provides enough details, **generate a full recruiting sequence**.
            - If details are missing, **ask a relevant follow-up question** before proceeding.  
            - If the user wants modifications, **refine the existing sequence instead of rewriting from scratch**.  

            **Tone & Style:**  
            - Be proactive in **gathering necessary information** and offering specific, actionable advice.  
            - **Ask one question at a time** to maintain clarity and engagement.  
            - Maintain a **professional, supportive, and insightful** tone. 
            - If the user asks for a sequence, ask for the hiring need first.

            **Your Decision:**  
            - If enough details are provided, generate a structured recruiting outreach sequence.  
            - If not, ask a relevant follow-up question.  
            - If the user is refining, update the existing sequence instead of rewriting from scratch. 
        """
    }

    # Construct the messages array
    messages = [system_message] + conversation_history + [
        {"role": "user", "content": user_message}
    ]
    
    # Get the response from OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.5
    )
    
    # Return both the response and the updated conversation history
    assistant_response = response.choices[0].message.content
    conversation_history.append({"role": "user", "content": user_message})
    conversation_history.append({"role": "assistant", "content": assistant_response})
    
    return assistant_response, conversation_history
