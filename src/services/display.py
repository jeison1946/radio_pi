from datetime import datetime
from time import sleep
from src.utils.lcd import LCD


def display():
    lcd = LCD()

    try:

        # logger.info('Player started!')

        lcd.clear()
        lcd.begin(16, 1)
        # Start the main program in an infinite loop
        while True:
            # status = run_cmd(cmd_check_device, True)
            # status = status[:4]

            lcd.clear()
            lcd.message("Escuchas:\n")
            sleep(2)

            # Show Serial
            lcd.clear()
            lcd.message("Serial:\n")
            sleep(3)

            # Show IP info
            lcd.clear()
    except Exception as e:
        lcd.clear()
        raise e
        display()
