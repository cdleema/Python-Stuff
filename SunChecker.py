from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
from win10toast import ToastNotifier
import time

while True:
    #Grabbing website
    url = 'https://www.timeanddate.com/astronomy/canada/brampton'

    content = urlopen(url).read()
    soup = BeautifulSoup(content,"html.parser")


    #Taking Setting Time for Sun #container[0]- sunrise, [1]- sunset, [2]-moon rise [3]-moon set
    container = soup.findAll('span',{'class':'three'})

    sunrise_time = container[0].string
    sunset_time = container[1].string

    #Getting time of sunset (as string)
    out = sunset_time.split(':')
    out[1].split(' ')
    hour_set = int(out[0]) + 12
    min_set = int(out[1][0])
    time_set = hour_set * 100+ min_set
##    print("The sun sets at",hour_set,"hr",min_set,"mins",time_set)

    #Getting time of sunrise(as string)
    out = sunrise_time.split(':')
    out[1].split(' ')
    hour_rise = int(out[0])
    min_rise = int(out[1][0])
    time_rise = hour_rise * 100 + min_rise
##    print("The sun rises at",hour_rise,"hr",min_rise,"mins",time_rise)

    #getting current time
    current_time = datetime.now()
    hour_now = current_time.hour
    min_now = current_time.minute
    time_now = hour_now * 100 + min_now
##    print("The time now is",hour_now,"hr",min_now,"mins", time_now)

##    #getting the date (to see if it's next day)
##    date_site = int(soup.find('span',{'id':'smct'}).string.split(' ')[1].split(',')[0])
##    date_now = int(current_time.day)

##    #time_now set here to Debug
##    time_now = 300

    sun_status = "The sun has not set today"
    sleep_time = 1800
    #Checking if sun has set
    if(time_now < time_rise):
        sun_status = "The sun has not yet risen"
    else:
        if(time_now >= time_set):
            sun_status = "The sun has set for today"
            sleep_time = 5400
            
##    print(sun_status,sleep_time)
    toaster = ToastNotifier()
    toaster.show_toast(sun_status,"Next reminder in " + str(sleep_time))
    time.sleep(sleep_time)
    
