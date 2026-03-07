from abc import ABC, abstractmethod
import os
from typing import List
from pydantic import BaseModel
from openai import AsyncOpenAI

class Message(BaseModel):
    role: str
    content: str

class AIProvider(ABC):
    @abstractmethod
    async def generate_response(self, messages: List[Message]) -> str:
        """
        Takes a list of message objects and returns the response string.
        """
        pass

class DeepSeekProvider(AIProvider):
    def __init__(self):
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
            
        # DeepSeek often provides an OpenAI-compatible API endpoint
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com" # Use standard Deepseek API base
        )
        self.model = "deepseek-chat" # Default chat model

    async def generate_response(self, messages: List[Message]) -> str:
        formatted_messages = [{"role": msg.role, "content": msg.content} for msg in messages]
        
        # Add a system prompt if none is present to guide it as an academic writing assistant
        if not any(msg["role"] == "system" for msg in formatted_messages):
            formatted_messages.insert(0, {
                "role": "system",
                "content": "You are a helpful and expert academic writing assistant. Your goal is to help the user improve their academic writing, clarify their arguments, and suggest better phrasing. Be concise but insightful."
            })

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=formatted_messages,
            max_tokens=2048,
            temperature=0.7
        )
        
        return response.choices[0].message.content

def get_ai_provider(provider_name: str = "deepseek") -> AIProvider:
    """Factory to get the requested AI provider."""
    # This allows for easy addition of OpenAI, Anthropic, etc. later
    if provider_name.lower() == "deepseek":
        return DeepSeekProvider()
    else:
        raise ValueError(f"Unsupported AI provider: {provider_name}")
