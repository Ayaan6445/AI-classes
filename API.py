import requests
import time

print("=====================================")
print("🤖Welcome to API Data Fetching Activity🤖")
print("=====================================")
print("This program fetches live data from a public APIs.")
print("You can choose to get jokes  or trivia questions!")
print("=============================================n")

def get_joke():
    """Fetch a random joke from the Chuck Norris API."""
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("\n😂 Heres your random joke:")
        print(data["value"])
    else:
        print("\n⚠️ Sorry! could not fetch a joke right now.")

def get_trivia():
     """Fetch a random question from the Open Trivia Database API."""
     url = "https://opentdb.com/api.php?amount=1&type=boolean"
     response = requests.get(url)
   
     if response.status_code == 200:
        data = response.json()
        question = data["results"][0]["question"]
        answer = data["results"][0]["correct_answer"]
        
        print("\n🧠 Trivia Time!")
        print("Question:", question)
        time.sleep(1)
        print("Answer", answer)
     else:
        print("\n⚠️ Unable to fetch trivia data right now")

     while True:
        print("\n choose an option:")
        print("1️⃣Get a random joke")
        print("2️⃣Get a trivia question")
        print("3️⃣Exit the program")

        choice = input("Enter your choice(1/2/3)").strip()

        if choice == "1":
            get_joke()
        elif choice == "2":
            get_trivia()
        elif choice == "3":
            print("\n👏 Thank you for using the API fetcher! Goodbye")
            break
        else:
            print("\n❌ Invalid choice! Please select 1, 2, or 3.")