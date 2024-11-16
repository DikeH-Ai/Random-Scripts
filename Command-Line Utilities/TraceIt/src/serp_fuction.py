import inquirer  # type: ignore
from pprint import pprint
import time
import threading
from pynput.keyboard import Controller, Key  # type: ignore


def set_timer(answer: list, default: bool):
    try:
        time.sleep(7)
        if answer[0] == None:
            print(f"\nTimeout! Using default answer")
            answer[0] = default
            keyboard_controller = Controller()
            keyboard_controller.press(Key.enter)
            keyboard_controller.release(Key.enter)
    except Exception as e:
        print(f"An error has occured(func: set_timer): {str(e)}")


def question_timer() -> bool:
    try:
        question = [
            inquirer.Confirm("setup", message="Set custom parameters")
        ]
        answers = [None]
        timer_thread = threading.Thread(
            target=set_timer, args=(answers, False))
        timer_thread.daemon = True
        timer_thread.start()

        ans = inquirer.prompt(question)

        if ans:
            answers[0] = ans["setup"]

        return answers[0]
    except Exception as e:
        print(f"An error has occured(func: set_timer): {str(e)}")


def custom_parameters():
    try:
        question = [
            inquirer.List('location',
                          message="location",
                          choices=[None, "Andorra", "United Arab Emirates", "Albania", "Armenia", "American Samoa", "Austria", "Azerbaijan", "Bosnia and Herzegovina", "Belgium", "Burkina Faso"]),
            # inquirer.List('',
            #               message="",
            #               choices=[]),
            # inquirer.List('',
            #               message="",
            #               choices=[]),
            # inquirer.List('',
            #               message="",
            #               choices=[]),
            # inquirer.List('',
            #               message="",
            #               choices=[]),
            # inquirer.List('',
            #               message="",
            #               choices=[]),
            # inquirer.List('',
            #               message="",
            #               choices=[]),
            # inquirer.List('',
            #               message="",
            #               choices=[]),
        ]
        answers = inquirer.prompt(question)

        pprint(answers)
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


if __name__ == "__main__":
    choice = question_timer()
    pprint(choice)
    if choice:
        parameters = custom_parameters()
    else:
        parameters = default_parameters()
    # result_json = serp_search(parameters)
