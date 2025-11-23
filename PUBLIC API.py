import requests
import random
import html

print("🎉 Welcome to the Trivia Quiz! 🎉")
print("-----------------------------------")

score = 0
questions_to_ask = 5

for q in range(questions_to_ask):
    url = "https://opentdb.com/api.php?amount=1&type=multiple"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Failed to fetch question from API.")
        break

    data = response.json()
    question_data = data["results"][0]

    question = html.unescape(question_data["question"])
    correct_answer = html.unescape(question_data["correct_answer"])
    incorrect_answers = [html.unescape(ans) for ans in question_data["incorrect_answers"]]

    options = incorrect_answers + [correct_answer]
    random.shuffle(options)

    print(f"\n❓ Question {q+1}:")
    print(question)

    for i, option in enumerate(options, 1):
      print(f"{i}. {option}")
      user_choice = input("👉 Enter your answer (1-4): ")

if not user_choice.isdigit() or int(user_choice) not in [1, 2, 3, 4]:
    print("Invalid input! Question skipped.")
    continue

user_answer = options[int(user_choice) - 1]

if user_answer == correct_answer:
    print("✅ Correct!")
    score += 1
else:
    print(f"❌ Wrong! The correct answer was: {correct_answer}")

print("\n------------------------------")
print(f"🏁 Quiz Finished! Your Score: {score}/{questions_to_ask}")
print("🎉 Thank you for playing! 🎉")

