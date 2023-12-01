import os
import re
import requests
from datetime import datetime

power_state = ""

def check_power_state(power_state):
    check_power_status = os.popen("pmset -g batt").read()
    power_source = re.search("(?<=').*(?=')", check_power_status).group(0)
    power_level = int(re.search("\\d{1,3}(?=%)", check_power_status).group(0))
    
    # Conditions here:
    # 1. Battery Power and Low Battery = Turn on the charger
    # 2. AC Adapter and Fully charged (100%) = Turn off the charger

    if(power_source == "Battery Power" and power_level <= 25):
        # Change the value of the endpoint that will request to turn on the charger
        power_state = "https://maker.ifttt.com/trigger/ON_EVENT/json/with/key/YOUR_API_KEY"
        return power_state
    elif(power_source == "AC Power" and power_level == 100):
        # Change the value of the endpoint that will request to turn off the charger
        power_state = "https://maker.ifttt.com/trigger/OFF_EVENT/json/with/key/YOUR_API_KEY"
        return power_state
    else:
        pass

requests.get(check_power_state(power_state))