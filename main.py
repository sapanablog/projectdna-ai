import asyncio

from agent import agent, AgentDeps


async def main():

    history = []
    deps = AgentDeps()

    print("=" * 50)
    print("🚀 Welcome to ProjectDNA-AI")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("\n👋 Goodbye!")
            break

        result = await agent.run(
            user_input,
            message_history=history,
            deps=deps,
        )

        history = result.all_messages()
        print(f"History length: {len(history)}")

        print(f"\nAssistant:\n{result.output}")


if __name__ == "__main__":
    asyncio.run(main())