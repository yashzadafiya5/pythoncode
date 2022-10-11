#remind me for time 9 to 5

import time
from plyer import notification

if __name__=="__main__":
    i=0
    while i<=24:
        notification.notify(
            title = "please drink water",
            message='''How much water should you drink a day? You probably know that it's important to drink plenty of fluids when the temperatures soar outside. But staying hydrated is a daily necessity, no matter what the thermometer says.''' ,
            app_name="yash i remind you please drink water",
            ticker=("please you drink water ") ,

            # displaying time
            timeout=2
        )
        time.sleep(30)
        notification.notify(
            title = "please eat your brakfast",
            message='''brakfast is a morning food and you need a energy for ''' ,
            app_name="yash i remind you please eat your food",
             

            # displaying time
            timeout=2
        )
        # waiting time
        time.sleep(3600)
        i+=1