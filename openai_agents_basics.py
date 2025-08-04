from agents import Agent, Runner
def main():

    agent = Agent(
        name='Assistant',
        instructions='You are a helpful assistant. Always maintain memory of the conversation history and remember the user\'s name is Dabid.',
        model="gpt-4o-mini", 
        )
    
    messages = []
    user_input = ""
    while user_input.lower() != "bye":
        user_input = input("\nYou: ")
        messages.append({"role": "user", "content": user_input})
        print("Assistant: ", end="")
        result = Runner.run_sync(
            agent, 
            input=messages
        )
        assistant_response = str(result.final_output)
        print(assistant_response)
        messages.append({"role": "assistant", "content": assistant_response})

# Run it
if __name__ == "__main__":
    main()
