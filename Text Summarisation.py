import requests
import json
from colorama import Fore, Style, init

init(autoreset=True)

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
API_TOKEN = "YOUR_HUGGINGFACE_API_TOKEN"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def print_header():
    print(Fore.CYAN + Style.BRIGHT + "\n📄 TEXT SUMMARIZATION TOOL")
    print(Fore.CYAN + "-" * 40)

def get_user_input():
    print(Fore.YELLOW + "\nEnter the text you want to summarize:")
    text = input(Fore.WHITE)

    min_len = int(input(Fore.YELLOW + "Enter minimum summary length: "))
    max_len = int(input(Fore.YELLOW + "Enter maximum summary length: "))

    return text, min_len, max_len

def send_request(text, min_len, max_len):
    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_len,
            "max_length": max_len
        }
    }

    response = requests.post(
        API_URL,
        headers=headers,
        data=json.dumps(payload)
    )

    return response

def handle_response(response):
    if response.status_code == 200:
        result = response.json()
        return result[0]["summary_text"]
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")

def main():
    try:
        print_header()
        text, min_len, max_len = get_user_input()

        print(Fore.BLUE + "\n⏳ Sending request to AI model...")
        response = send_request(text, min_len, max_len)

        summary = handle_response(response)

        print(Fore.GREEN + Style.BRIGHT + "\n✅ SUMMARY OUTPUT")
        print(Fore.GREEN + "-" * 40)
        print(Fore.WHITE + summary)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + "\n❌ ERROR")
        print(Fore.RED + str(e))
    
if __name__ == "__main__":
    main()