from typing import Any, Callable

from pydantic_ai.capabilities import AbstractCapability
from pydantic_ai.settings import ModelSettings
from pydantic_ai.tools import RunContext


class ReasoningEffort(AbstractCapability[Any]):
    """Dynamically adjusts reasoning effort based on the user's request."""

    def get_model_settings(self) -> Callable[[RunContext[Any]], ModelSettings]:

        def _set_reasoning_effort(ctx: RunContext[Any]) -> ModelSettings:

            prompt = (ctx.prompt or "").lower()

            low_keywords = [
                "hello",
                "hi",
                "thanks",
                "thank you",
                "quick",
                "simple",
                "short",
            ]

            high_keywords = [
                "design",
                "architecture",
                "analyse",
                "analyze",
                "debug",
                "explain",
                "implement",
                "compare",
                "optimize",
                "algorithm",
                "project",
                "system",
                "performance",
                "scalable",
            ]

            if len(prompt) > 120:
                effort = "high"
            elif any(k in prompt for k in high_keywords):
                effort = "high"
            elif any(k in prompt for k in low_keywords):
                effort = "low"
            else:
                effort = "medium"

            print("=" * 40)
            print(f"🧠 Reasoning Level: {effort.upper()}")
            print("=" * 40)

            return ModelSettings(thinking=effort)

        return _set_reasoning_effort