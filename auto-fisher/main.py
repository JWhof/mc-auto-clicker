import pyautogui as pag
import time
from pynput import keyboard
import threading

COUNTDOWN_TIME = 3 # time to tab into Minecraft in seconds

FOOD_HOTKEY = '8' # hotkey to access food as str
NUM_FOOD = 64 # number of food in food hotkey
SECONDS_BETWEEN_CLICKS = 3
DISCONNECT_X = 0 # X coord of disconnect btn
DISCONNECT_Y = 0 # Y coord of disconnect btn

DURABILITY_OF_RODS = 65
DURABILITY_OF_SWORDS = 250


def main():
    'Runs the afk auto clicker program.'
    
    def prompt():
        program_function = input("Welcome to the afk auto clicker program! Please remember to \
            Input 1 to farm mobs, 2 to afk fish, or 3 to exit the program.")
        if program_function == "1":
            Clicker.start_clicker(Clicker.farm_mobs(seconds_between_clicks=SECONDS_BETWEEN_CLICKS))
        elif program_function == "2":
            Clicker.start_clicker(Clicker.afk_fish())
        elif program_function == "3":
            print("Exiting the program.")
            exit()
        else:
            prompt()


    def start_up(time_to_wait: int):
        'Prints a countdown to give the user time to tab back in.'
        for seconds_left in range(time_to_wait)[::-1]:
            print(f"{seconds_left+1}...")
            time.sleep(1)
        print("starting.........")
        time.sleep(1)



    class Clicker():

        def __init__(self):
            self.num_clicks = 0
            self.fish_caught = 0
            self.item_number = 0
            self.food_eaten = 0

        def farm_mobs(self, seconds_between_clicks):
            'Clicks every x seconds, listens for key press.'
            stop_event = threading.Event()

            def click_loop():
                while not stop_event.is_set():
                    pag.click()
                    self.num_clicks += 1

                    if time.time() - self.starting_time % 1200 == 0:
                        self.eat_food()
                        self.food_eaten += 1
                        time.sleep(1)
                    
                    if self.food_eaten >= NUM_FOOD:
                        self.disconnect()
                    
                    if self.num_clicks >= DURABILITY_OF_SWORDS:
                        pag.scroll(1) # TODO: check that this works
                        self.item_number += 1
                        self.num_clicks = 0
                    
                    if self.item_number >= 9:
                        self.disconnect()

                    self.num_clicks += 1
                    time.sleep(seconds_between_clicks)
            
            click_thread = threading.Thread(target=click_loop)
            click_thread.start()

            with keyboard.Listener(on_press=lambda key: stop_event.set()) as listener:
                while not stop_event.is_set():
                    for _ in range(int(seconds_between_clicks / 0.1)):
                        if stop_event.is_set():
                            break
                        time.sleep(0.1)
                    if stop_event.is_set():
                        break

            stop_event.set()
            click_thread.join()

        def afk_fish(self):
            'Holds to right mouse button.'
            pag.mouseDown()


            if time.time() - self.starting_time % 1200 == 0:
                self.eat_food()
                self.food_eaten += 1
                time.sleep(1)

            if self.food_eaten >= NUM_FOOD:
                self.disconnect()

            if time.time() - self.starting_time % 25 == 0:
                self.fish_caught += 1
                time.sleep(1)

            if self.fish_caught >= DURABILITY_OF_RODS:
                pag.scroll(1) # TODO: check that this works
                self.item_number += 1
                self.fish_caught = 0
                
            if self.item_number >= 9:
                self.disconnect(DISCONNECT_X, DISCONNECT_Y)
                

        def start_clicker(self, action_once_key_pressed, seconds_between_clicks=1):
            'Starts clicker, stops clicking once f pressed and performs specified action.'
            start_up(COUNTDOWN_TIME)
            self.starting_time = time.time()



            stop_event = threading.Event()

            def action(event_stop):
                pass

            with keyboard.Listener(on_press=lambda key: action()) as listener:
                while not stop_event.is_set(): 
                    action(event_stop=stop_event)



            if action_once_key_pressed == self.afk_fish:
                stop_event = threading.Event()

                def stop_fishing():
                    print("stopping current action, f key was pressed")
                    pag.mouseUp()
                    stop_event.set()

                with keyboard.Listener(on_press=lambda key: stop_fishing()) as listener:
                    while not stop_event.is_set():
                        self.afk_fish()
                        listener.join(0.1)

                stop_event.set()

            else:
                self.farm_mobs(seconds_between_clicks)


        def eat_food(current_key: str, food_hotkey: str):
            'Eats food in a specified position in the hotbar, returns food remaining.'
            pag.press(food_hotkey)
            pag.mouseDown(button='right')
            time.sleep(1.75)
            pag.mouseUp()
            pag.press(current_key)

        def disconnect(disconnect_x, disconnect_y):
            'Disconnects the user from the game.'
            pag.press('esc')
            pag.moveTo(disconnect_x, disconnect_y)
            pag.click()
            print("Exiting the program.")
            exit()


        

    
    
    


if __name__ == "__main__":
    main()