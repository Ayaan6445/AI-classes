import requests

def get_json_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    data = response.json()
    return data["text"]

def get_text_fact():
    url = "https://uselessfacts.jsph.pl/random.txt?language=en"
    response = requests.get(url)
    return response.text.strip()

def get_today_fact():
    url = "https://uselessfacts.jsph.pl/today.json?language=en"
    response = requests.get(url)
    data = response.json()
    return data["text"]

def get_german_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=de"
    response = requests.get(url)
    data = response.json()
    return data["text"]

print("🧠 Exploring Different Endpoints in Facts API’s")
print("Type 'exit' to quit.\n")

menu = """
Choose an option:
1. Get Random Fact (JSON)
2. Get Random Fact (Text)
3. Get Today’s Fact
4. Get Random Fact in German
Enter your choice: """

while True:
    choice = input(menu)

    if choice.lower() == "exit":
        print("Goodbye!")
        break

    if choice == "1":
        print("\n🟦 JSON FACT:\n", get_json_fact())
    elif choice == "2":
        print("\n🟩 TEXT FACT:\n", get_text_fact())
    elif choice == "3":
        print("\n🟨 TODAY'S FACT:\n", get_today_fact())
    elif choice == "4":
        print("\n🇩🇪 GERMAN FACT:\n", get_german_fact())
    else:
        print("❌ Invalid choice, try again.")

    print("-" * 60)
