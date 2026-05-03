import requests

OLLAMA_SERVER = "http://localhost:11434"
MODEL_NAME = "qwen3:4b"

def main():
    print("CLI Chatbot (type 'exit' to quit)\n")

    messages = []

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})

        response = requests.post(
            f"{OLLAMA_SERVER}/api/chat",
            json={
                "model": MODEL_NAME,
                "messages": messages,
                "stream": False
            }
        )

        result = response.json()
        bot_reply = result["message"]["content"]

        print("\nBot:", bot_reply, "\n")

        messages.append({"role": "assistant", "content": bot_reply})

if __name__ == "__main__":
    main()