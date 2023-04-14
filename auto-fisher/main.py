import pyautogui as pag
import time
import threading

CONFIDENCE = 0.9
TIME_TO_SLEEP = 1472 # 64 durability x 23s/catch = 1472

def main():

    def start_up(): # wait desired number of seconds and display countdown
        for seconds_left in range(3)[::-1]:
            print(f"{seconds_left+1}...")
            time.sleep(1)
        print("starting.........")
        time.sleep(1)

    start_up()

    pag.mouseDown(button='right') # hold down right mouse button

    count = 0
    for i in range(9):
        try:
            pag.locate('auto-fisher\\rod_screenshot.png', pag.screenshot(), confidence=CONFIDENCE)
            print('located fishing rod, sleeping 10s')
            time.sleep(TIME_TO_SLEEP) # wait until fishing rod breaks
            pag.press(f'{count+1}')
            print(f'count: {count}')
            count += 1
        except:
            break

    pag.mouseUp(button='right')


if __name__ == "__main__":
    main()