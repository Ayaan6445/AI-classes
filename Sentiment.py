from textblob import TextBlob

print(" Welcome to the Simple sentiment analyzer!")
name = input ("Whats your name")
print(f"Nice to meet you, {name}! Lets find out the sentiment of your senetences")
print("Type 'exit' to quit.\n")
while True:
    sentence = input("Your sentence")
    if sentence. lower () == 'exit':
        print(f"Goodbye, {name}! ")
        break
    blob = TextBlob (sentence)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print("Positive sentiment detected! \n")
    elif sentiment < 0:
        print("Negative sentiment detected! \n")
    else:
        print("Neutral sentiment detected! \n")