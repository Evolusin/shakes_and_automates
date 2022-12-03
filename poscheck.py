import pyautogui



while True:
    print(pyautogui.mouseInfo())

    if pyautogui.keyDown("q"):
        exit()