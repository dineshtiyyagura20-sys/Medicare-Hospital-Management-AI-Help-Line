import os
from groq import Groq
from dotenv import load_dotenv # call .env file
from system_prompt import SYSTEM_PROMPT
# Load variables from .env
load_dotenv()  # call our API_KEY

def get_client():
    """
    Create and return a Groq client.

    The API key is read from the GROQ_API_KEY
    environment variable.
    """

    api_key = os.getenv("GROQ_API_KEY") # store api_key by variable

    if not api_key: # check the the key does exist or not ?
        return None

    return Groq(api_key=api_key)


def ask_medicare_ai(user_message, conversation_history=None):
    """
    Send a user question to the MediCare AI Help Line.

    Parameters:
        user_message (str):
            The latest question from the user.

        conversation_history (list):
            Previous conversation messages.

    Returns:
        str:
            AI response or an error message.
    """

    client = get_client()

    if client is None:
        return (
            "⚠️ Groq API key is not configured.\n\n"
            "Please add GROQ_API_KEY to your .env file."
        )

    if conversation_history is None:
        conversation_history = []

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # Add previous conversation
    for message in conversation_history:

        # Only allow valid chat roles
        if message.get("role") in ["user", "assistant"]:
            messages.append(
                {
                    "role": message["role"],
                    "content": message["content"]
                }
            )

    # Add current question
    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            temperature=0.3,
            max_completion_tokens=500,
            include_reasoning=False
        )

        return response.choices[0].message.content
    

    except Exception as error:
        return (
            " Unable to connect to the MediCare AI Help Line.\n\n"
            f"Error: {str(error)}"
        ) 
    