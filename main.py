import pyautogui as pag
import time

COUNTDOWN_TIME = 3 # time to tab into Minecraft in seconds

FOOD_HOTKEY = '8' # hotkey to access food as str


def main():
    'Runs the afk auto clicker program.'
    
    def prompt():
        program_function = input("Welcome to the afk auto clicker program! Please remember to \
            Input 1 to farm mobs, 2 to afk fish, or 3 to exit the program.")
        if program_function == "1":
            farm_mobs()
        elif program_function == "2":
            afk_fish()
        elif program_function == "3":
            print("Exiting the program.")
            exit()
        else:
            prompt()
        return

    def start_up(time_to_wait: int):
        'Prints a countdown to give the user time to tab back in.'
        for seconds_left in range(time_to_wait)[::-1]:
            print(f"{seconds_left+1}...")
            time.sleep(1)
        print("starting.........")
        time.sleep(1)
        return

    def eat_food(current_key: str, food_hotkey: str):
        'Eats food in a specified position in the hotbar, returns food remaining.'
        pag.press(food_hotkey)
        pag.mouseDown(button='right')
        time.sleep(1.75)
        pag.mouseUp()
        pag.press(current_key)
        return

    def farm_mobs(seconds_between_clicks):
        'Clicks every x seconds, changes weapon after it breaks.'
        pass

    def afk_fish():
        'Holds to right mouse button, changes rod after it breaks.'
        pass

    def disconnect(disconnect_x, disconnect_y):
        'Disconnects the user from the game.'
        pag.press('esc')
        pag.moveTo(disconnect_x, disconnect_y)
        pag.click()
        print("Exiting the program.")
        exit()
    
    


if __name__ == "__main__":
    main()