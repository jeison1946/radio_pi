from datetime import datetime
from time import sleep
from src.utils.lcd import LCD;
from src.services.network_service import NetworkService;
from src.services.config_service import ConfigService

def display():
    lcd = LCD();
    network_service: NetworkService = NetworkService()
    lcd.clear()
    lcd.begin(16, 1)
    try:
        config: ConfigService = ConfigService();
        # logger.info('Player started!')

        lcd.clear()
        lcd.begin(16, 1)
        # Start the main program in an infinite loop
        while True:
            # status = run_cmd(cmd_check_device, True)
            # status = status[:4]
            lcd.clear()
            lcd.message(config.get_brand() + "\n")
            sleep(2)

            lcd.clear()
            lcd.message("Escuchas:\n")
            sleep(2)

            # Show Serial
            lcd.clear()
            lcd.message("Serial:\n")
            lcd.message(config.get_serial())
            sleep(3);

            lcd.clear()
            ipaddr = network_service.get_ipaddress()

            if not ipaddr:
                lcd.message('Sin Internet\n')
            else:
                lcd.message(ipaddr + "\n")

            # Show IP info
            i = 0
            while i < 3:
                lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
                sleep(1)
                i = i+1
                pass
    except Exception as e:
        lcd.clear();
        raise e
        display()
