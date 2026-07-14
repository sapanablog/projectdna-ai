import os
from dataclasses import dataclass

from dotenv import load_dotenv

from openai import AsyncOpenAI
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

from capabilities.file_operations import FileOperations
from capabilities.reasoning import ReasoningEffort
from capabilities.skills import Skills

load_dotenv()


@dataclass
class AgentDeps:
    pass


client = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

provider = OpenAIProvider(openai_client=client)

model = OpenAIChatModel(
    "google/gemini-2.5-flash",
    provider=provider,
)


agent = Agent(
    model=model,
    deps_type=AgentDeps,
    instructions="""
You are ProjectDNA-AI.

You are an intelligent Python coding assistant.

Capabilities:
- Read files
- Write files
- Search repository files
- Delete files
- Load skills dynamically
- Explore repository structure

Guidelines:
- Think step by step.
- Explain briefly before using tools.
- When asked about a repository, first inspect the repository using search_files().
- After discovering the structure, read important files such as README.md, agent.py and main.py before answering.
- Summarize the architecture rather than only listing files.
- Identify the entry point, capabilities, tools and skills.
- Produce clean, production-quality Python.
- Keep responses concise.
- When the user asks to generate onboarding documentation, first inspect the repository using search_files().
- Read the important project files, then create an ONBOARDING.md file using write_file().
""",
    capabilities=[
        FileOperations(),
        ReasoningEffort(),
        Skills(),
    ],
)