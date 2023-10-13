import requests

# Set the URL of your Rasa chatbot endpoint
rasa_endpoint = "http://localhost:5005/webhooks/rest/webhook"  # Update this with your Rasa endpoint URL

# Send a message to the chatbot
def send_message(message):
    payload = {
        "sender": "user",
        "message": message,
    }

    response = requests.post(rasa_endpoint, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Main interaction loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Exiting the chatbot.")
        break

    response = send_message(user_input)

    if response:
        for message in response:
            if "text" in message:
                print(f"Bot: {message['text']}")
    else:
        print("Error: Unable to communicate with the chatbot.")
