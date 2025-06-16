from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import re


service = Service(ChromeDriverManager().install())

# URLS
with open("urls.txt", "r", encoding="utf-8") as f:
    URLS = f.readlines()


def extract_first_two_numbers(url: str) -> str:
    # Find all numbers in the URL using regex
    numbers = re.findall(r"\d+", url)

    # Check if we have at least two numbers
    if len(numbers) < 2:
        return "Less than two numbers found in the URL."

    # Return formatted string with the first two numbers
    return f"Week {numbers[0]}, Day {numbers[1]}"


def get_workout(URL: str):

    driver.get(URL)
    time.sleep(15)
    page_text = driver.find_element("tag name", "body").text
    # Split the text into lines
    lines = page_text.splitlines()

    # Remove top 2 and bottom 15 lines
    trimmed = lines[2:-15]

    fname = "workouts/" + extract_first_two_numbers(URL) + ".txt"
    with open(fname, "w", encoding="utf-8") as f:
        f.writelines([line + "\n" for line in trimmed])


if __name__ == "__main__":

    driver = webdriver.Chrome(service=service)

    [get_workout(url) for url in URLS]

    driver.close()
