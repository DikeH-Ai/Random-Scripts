import inquirer  # type: ignore
from pprint import pprint
import time
import threading
from pynput.keyboard import Controller, Key  # type: ignore
from rapidfuzz import process  # type: ignore


def set_timer(answer: list, default: bool):
    """
        Automatic input after 7 seconds without a user input
        failsafe for autonomous operation
    """
    try:
        time.sleep(7)
        if answer[0] == None:
            print(f"\nTimeout! Using default answer")
            answer[0] = default
            # press Enter key
            keyboard_controller = Controller()
            keyboard_controller.press(Key.enter)
            keyboard_controller.release(Key.enter)
    except Exception as e:
        print(f"An error has occured(func: set_timer): {str(e)}")


def question_timer() -> bool:
    """
        Modify user settings-> True or False
    """
    try:
        question = [
            inquirer.Confirm("setup", message="Set custom parameters")
        ]
        answers = [None]
        # using another process to call the timer
        timer_thread = threading.Thread(
            target=set_timer, args=(answers, False))
        timer_thread.daemon = True
        # start function
        timer_thread.start()

        # response is assinged to ans
        ans = inquirer.prompt(question)
        # if user response before the timer runs down
        if ans:
            answers[0] = ans["setup"]

        return answers[0]
    except Exception as e:
        print(f"An error has occured(func: set_timer): {str(e)}")


def custom_parameters():
    """
        Setup;
            "Geographic Location":
            "Localization":,
            "Pagination":,
            "Advanced Parameters":,
            "Advanced Filters":,
            "SerpApi Parameters":
        settings
    """
    try:
        # each function dictionary holder
        func_dict = {
            "Geographic Location": geo_location,
            # "Localization":,
            # "Pagination":,
            # "Advanced Parameters":,
            # "Advanced Filters":,
            # "SerpApi Parameters":
        }
        # parameters

        parameters = {
            "engine": "google_reverse_image",
            "image_url": None,
            "api_key": "secret_api_key"
        }
        question = [
            inquirer.List('settings',
                          message="Select Settings",
                          choices=[None, "Geographic Location", "Localization", "Pagination", "Advanced Parameters", "Advanced Filters", "SerpApi Parameters"]),
        ]
        answers = inquirer.prompt(question)

        pprint(answers)
        parameters.update(answers["settings"]())
    except Exception as e:
        print(f"An error has occured(func: set_timer): {str(e)}")


def default_parameters() -> dict:
    """
        Use the default query parameters
    """
    parameters = {
        "engine": "google_reverse_image",
        "image_url": None,
        "api_key": "secret_api_key"
    }
    print("In default")
    return parameters


"""
    Each custom settings
"""


def geo_location() -> dict:
    try:
        question = [
            inquirer.List('option', message="Select Settings: ",
                          choices=["location", "uule"])
        ]
        answers = inquirer.prompt(question)

        if answers["option"] == "location":
            # get location list
            locations = []
            with open("./data/locations_list.txt", "r",  encoding="utf-8") as file:
                locations = file.readlines()
            locations = [location.strip() for location in locations]

            question1 = [
                inquirer.Text(
                    'location', message="Location(Enter for None)", default=None)
            ]

            input_text = inquirer.prompt(question1)
            matches = get_top_matches(input_text["location"], locations)
            matches = [match[0] for match in matches]
            matches.append(None)
            question2 = [
                inquirer.List(
                    'locations', message="Select Location", choices=matches)
            ]
            selected_loc = inquirer.prompt(question2)
            return selected_loc
        else:
            questions = [
                inquirer.Text('uule',
                              message="Input uule: "),
            ]

            uule_dict = inquirer.prompt(questions)
            return uule_dict
    except Exception as e:
        print(f"An error has occured: {str(e)}")
        return

# Function to get the top 10 closest matches using fuzzywuzzy


def get_top_matches(user_input, location_list, top_n=10):
    matches = process.extract(user_input, location_list, limit=top_n)
    return matches


if __name__ == "__main__":
    # choice = question_timer()
    # pprint(choice)
    # if choice:
    #     parameters = custom_parameters()
    # else:
    #     parameters = default_parameters()
    location = geo_location()
    print(location)
    # result_json = serp_search(parameters)
