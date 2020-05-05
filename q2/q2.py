import urllib
from urllib import request
from bs4 import BeautifulSoup
import subprocess
import datetime
def weather(city):
    the_url = "https://www.timeanddate.com/weather/india/" + city
    the_page = urllib.request.urlopen(the_url)
    soup = BeautifulSoup(the_page, "html.parser")
    content = soup.findAll('div', {"class": "three columns"})[0]
    #print (content)
    garbage = content.find('div', {'class': 'h2'}).text
    weather_condition = str(content.findAll('p')[0].text)
    tempa = garbage.split(" ")[0].encode('ascii', 'ignore').decode()
    return tempa,weather_condition
city = input()
tempa,weather_condition = weather(city)
weather_condition = weather_condition.lower()
t_degree=tempa[0:len(tempa)-1]
act=int(t_degree)
hourss = datetime.datetime.now()
hours= hourss.hour
print(hours)
print ("current time=",hours,"cureent_temp=",act,"current_weather=",weather_condition)
if act<10 and hours>4 and hours<18:
    subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format(r'/home/ankush/team47_assignment2/q2/image/day_cold.jpg'), shell=True)
if act<10 and hours>=18 and hours<=4:
    subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format(r'/home/ankush/team47_assignment2/q2/image/night_cold.jpg'), shell=True)
su_cloud='cloud'
su_sun='clear'
su_fog='fog'
su_rain='rain'
su_thunder='thunder'
su_storm='storm'
su_partly='sunny'
su_haze='haze'
cl=weather_condition.find(su_cloud)
su=weather_condition.find(su_sun)
ra=weather_condition.find(su_rain)
fo=weather_condition.find(su_fog)
th=weather_condition.find(su_thunder)
st=weather_condition.find(su_storm)
pa=weather_condition.find(su_partly)
ha=weather_condition.find(su_haze)
if act>10 and (hours>4 and hours<18):
    if cl != -1:
        print("in line 47")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/day_clould.jpg"), shell=True)
    elif su !=-1:
        print("in line 50")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/day_sun.jpg"), shell=True)
    elif ra !=-1:
        print("in line 53")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/rain.jpg"), shell=True)
    elif th!=-1:
        print("in line 56")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/thunder.jpg"), shell=True)
    elif st!=-1:
        print("in line 59")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/thunder.jpg"), shell=True)
    elif fo!=-1:
        print("in line 62")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/fog.jpg"), shell=True)
    elif pa != -1:
        print("in line 70")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/day_clould.jpg"), shell=True)
    elif ha != -1:
        print("in line 73")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/day_clould.jpg"), shell=True)
    else:
        print("in line 76")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/day_clould.jpg"), shell=True)

elif act>10 and (hours>=18 or hours<=4):
    if cl != -1:
        print("in line 81")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/night_cloud.jpg"), shell=True)
    elif su !=-1:
        print("in line 84")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/night_moon.jpg"), shell=True)
    elif ra !=-1:
        print("in line 87")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/night_rain.jpg"), shell=True)
    elif th!=-1:
        print("in line 90")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/thunder.jpg"), shell=True)
    elif st!=-1:
        print("in line 93")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/thunder.jpg"), shell=True)
    elif fo!=-1:
        print("in line 96")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/night_cold.jpg"), shell=True)
    elif ha != -1:
        print("in line 99")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/night_cloud.jpg"), shell=True)
    elif pa != -1:
        print("in line 102")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/night_cloud.jpg"), shell=True)
    else:
        print("in line 105")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/team47_assignment2/q2/image/night_cloud.jpg"), shell=True)
