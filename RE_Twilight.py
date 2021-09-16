# A script to trigger Twilight Sounds at sunset at a location
# September 15, 2021
# Able Kirby

verstr = "1.0"

import requests
from datetime import datetime
import time
import sys

# Return sunset time at location as seconds from last UTC midnight
def get_ss(latlong):
    req = "https://api.sunrise-sunset.org/json?" + \
            "lat=" + str(latlong[0]) + \
            "&lng=" + str(latlong[1]) + \
            "&date=today"
    obj = requests.get(req)

    ss = obj.json()["results"]["sunset"]
    ss = time.strptime(ss,"%H:%M:%S %p")
    ss = 3600*(12+ss.tm_hour) + 60*ss.tm_min + ss.tm_sec

    if obj.status_code == 200:
        return ss
    else:
        print("Unable to retreive sunset time")
        return 86410

# Get time now as seconds since last UTC midnight
def get_tnow():
    now = datetime.utcnow()
    seconds = 3600*int(now.strftime("%H")) + 60*int(now.strftime("%M")) + int(now.strftime("%S"))
    return seconds

def pretty_time(dt):
    # format duration as appropriate
    if dt > 3600:
        return f"{(ssEnd-tnow)/3600:.1f} hours"

    elif dt > 60:
        return f"{(ssEnd-tnow)/60:.1f} minutes"
    else:
        return f"{(ssEnd-tnow):.0f} seconds"




# Program start
print("RE_Twilight " + verstr)
print("Rare Encounter: Twilight Trigger")
print(f"Program Start: {get_tnow():.0f} seconds into day (UTC)")

# Today's Sunset times [via sunrise-sunset.org]
#ssStart = get_ss((39.278, -76.861)) # Maryland
#ssEnd = get_ss((43.91, -78.788)) # Courtise

ssStart = 17153
ssEnd = 17183

# Trigger
armed1 = True
armed2 = True
tlast = get_tnow()
while(1):
    tnow = get_tnow()

    if armed1 == True and tnow >= ssStart:
        armed1 = False
        print("--Twilight Begin warning")
        print("--Twilight Begin warning")
        print("--Twilight Begin warning")
        print("--Twilight Begin warning")
        print("--Twilight Begin warning")

    if armed2 == True and tnow >= ssEnd:
        armed2 = False
        print("--Twilight End warning")
        print("--Twilight End warning")
        print("--Twilight End warning")
        print("--Twilight End warning")
        print("--Twilight End warning")
        print("Clock will reset after UTC midnight")

    if armed1:
        print("Twilight Begins in " + pretty_time(ssStart-tnow))

    if armed2 and not armed1:
        print("Twilight Ends in " + pretty_time(ssEnd-tnow))
        
    if (tnow < tlast):
        # Re-arm each morning
        armed1 = True
        armed2 = True
        ssEnd = get_ss((43.91, -78.788))
        ssStart = get_ss((39.278, -76.861))

    tlast = tnow

    if abs(tnow-ssStart) > 3600:
        time.sleep(1800)
    elif abs(tnow-ssStart) > 60:
        time.sleep(30)
    else:
        time.sleep(1)