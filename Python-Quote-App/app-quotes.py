import requests
import time

def main():
    # api_url = "https://api.quotable.io/random"
    api_url = "https://zenquotes.io/api/quotes"
    while True:
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    # quote = data['content']
                    quote = data[0]['q']
                    author = data[0]['a']
                    print(f"Quote: {quote} - Author: {author}")
                else:
                    print("No quote found.")
            else:
                print(f"Error: Unable to fetch quote. Status code: {response.status_code}")
        except Exception as e:
            print(f"Exception occurred: {e}")
        time.sleep(30)  # Sleep for 60 seconds before fetching the next quote

if __name__ == "__main__":
    main()

# This script fetches a random quote from the ZenQuotes API every 60 seconds and prints it to the console.
# It handles exceptions and prints error messages if the API call fails.
# The script will run indefinitely until manually stopped.
# ZenQuotes API: https://zenquotes.io/
# Note: The API URL and the way to extract the quote may change, so make sure to check the API documentation for the latest information.
