import argparse
import requests

OLLAMA_SERVER = "http://localhost:11434"
MODEL_NAME = "qwen3:4b"

def main():
    parser = argparse.ArgumentParser(
        description="Send a CLI prompt to Ollama (LLaMA model running on server)"
    )
    parser.add_argument(
        "prompt",
        type=str,
        help="Prompt to send to the LLaMA model"
    )

    args = parser.parse_args()

    response = requests.post(
        f"{OLLAMA_SERVER}/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": args.prompt,
            "stream": False
        }
    )

    result = response.json()

    print("\n--- Response from local LLaMA model ---\n")
    print(result["response"])

if __name__ == "__main__":
    main()