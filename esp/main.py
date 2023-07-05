from esp_helper import *

while True:
    connect_wifi()
    check_battery()
    value = A2.read() / 4096.0
    print(value)
    sleep(.1)
#    hall = esp32.hall_sensor()
#    print(hall)
#    post_data("hall-sensor", hall)
