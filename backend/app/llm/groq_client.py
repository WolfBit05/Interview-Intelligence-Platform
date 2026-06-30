from groq import Groq
from dotenv import load_dotenv
import os
from app.prompts.rag_prompt import (
    RAG_SYSTEM_PROMPT,
    RAG_USER_PROMPT
)
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(question, context):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content": RAG_SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": RAG_USER_PROMPT.format(
                    context=context,
                    question=question
                )
            }
        ]
    )

    return response.choices[0].message.content