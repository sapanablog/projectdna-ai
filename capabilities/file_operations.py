from typing import Any

from pydantic_ai.capabilities import AbstractCapability
from pydantic_ai.toolsets import FunctionToolset
from pydantic_ai.tools import RunContext, ToolCallPart, ToolDefinition

from tools.file_tools import (
    read_file,
    write_file,
    search_files,
    delete_file,
)


class FileOperations(AbstractCapability[Any]):
    """Provides file system tools to the agent."""

    def get_toolset(self) -> FunctionToolset:
        toolset = FunctionToolset()
        toolset.add_function(read_file)
        toolset.add_function(write_file)
        toolset.add_function(search_files)
        toolset.add_function(delete_file)
        return toolset

    async def before_tool_execute(
        self,
        ctx: RunContext[Any],
        *,
        call: ToolCallPart,
        tool_def: ToolDefinition,
        args: dict[str, Any],
    ) -> dict[str, Any]:
        print(f"\n→ Calling tool: {call.tool_name}")
        print(f"   Arguments: {args}")
        return args