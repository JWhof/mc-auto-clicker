import pyautogui as pag
import time

DURABILITY_OF_SWORD1 = 200
DURABILITY_OF_OTHERS = 251
TIME_TO_WAIT = 3

def main():

    def start_up(): # wait desired number of seconds and display countdown
        for seconds_left in range(3)[::-1]:
            print(f"{seconds_left+1}...")
            time.sleep(1)
        print("starting.........")
        time.sleep(1)

    start_up()

    for i in range(DURABILITY_OF_SWORD1):
        pag.click()
        time.sleep(TIME_TO_WAIT)
        print("clicked")
    while True:
        count = 1
        pag.press(f'{count+1}')
        for i in range(DURABILITY_OF_OTHERS):
            pag.click()
            time.sleep(TIME_TO_WAIT)
            print("clicked")




if __name__ == "__main__":
    main()
