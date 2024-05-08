import datetime
import webbrowser

# Function to respond to user queries
def assistant_actions(query):
    if query:
        if "hello" in query.lower():
            print("Assistant: Hello! How can I assist you?")
        elif "time" in query.lower():
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Assistant: The current time is {current_time}")
        elif "date" in query.lower():
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            print(f"Assistant: Today's date is {current_date}")
        elif "search" in query.lower():
            print("Assistant: What do you want me to search for?")
            search_query = input("You: ")
            search_url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
            webbrowser.open(search_url)
        elif "exit" in query.lower():
            print("Assistant: Goodbye!")
            exit()

# Main function to run the assistant
def main():
    print("Assistant: Hello! I'm your voice assistant. How can I help you today?")
    while True:
        query = input("You: ")
        assistant_actions(query)

if __name__ == "__main__":
    main()

