import requests

def get_tech_fact():
   url = "https://techy-api.vercel.app/api/json"

   try:
      response = requests.get(url)
      data = response.json()

      return data.get("message", "No fact found")
   
   except Exception as e:
      return f"Error fetching fact: {e}"

print("💻 Welcome to the Random Technology Facts Activity!")
print("Type 'exit' to stop.\n")

while True:
   user = input("Press ENTER to get a tech fact or type 'exit':")

   if user.lower() == "exit":
      print("Goodbye!")
      break
   
   fact = get_tech_fact()
   print("\n⚡ TECHNOLOGY FACT:", fact)
   print("_" * 60)