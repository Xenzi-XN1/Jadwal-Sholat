# Open source hehe
# Code by xenzi Ganz
# Janggan lupa ngopi + follow github + subscribe >_<
from requests import get as _get_data_xenzi_
from requests import post as _post_data_xenzi_
from json import loads as _json_data_xenzi_
from os import system as _os_data_xenzi_
from time import sleep as _time_data_xenzi_

P1 = "\033[37;7;1m"
A1 = "\033[0m"
p = '\033[1;37m'
m = "\033[1;31m"
h = "\033[1;32m"
k = "\033[1;33m"
l = "\033[1;36m"
u = "\033[1;35m"
b = '\033[1;30m'
t = '\033[1;107m'
s = '\033[0m'

# url api Shortlink v1
url = "https://xenzi-ganz.herokuapp.com/api/jadwal_sh"
# download apikey nya dulu >_<
apikey = "Download apikey nya dulu >_< Trial"
logo = f"""
{m} ╦{p}┌─┐┌┬┐┬ ┬┌─┐┬    {l}┌─┐{p}┬ ┬┌─┐┬  ┌─┐┌┬┐
{m} ║{p}├─┤ │││││├─┤│    {l}└─┐{p}├─┤│ ││  ├─┤ │
{m}╚╝{p}┴ ┴─┴┘└┴┘┴ ┴┴─┘  {l}└─┘{p}┴ ┴└─┘┴─┘┴ ┴ ┴
 {m}• {p}Creator {m}: {p}Xenzi Ganz
 {m}• {p}Team {m}: {k}Team Xenzi
 {m}• {p}Blog {m}: {h}https://team-xenzi.blogspot.com
     {P1}https://xenzi-ganz.herokuapp.com/{A1}
"""

def Jadwal_Sholat():
     _os_data_xenzi_('clear')
     print (logo)
     print (f' {m}• {p}masukan nama daerah')
     daerah = input(f' {m}• {p}Daerah {m}:{h} ')
     api1 = _get_data_xenzi_(url, params={'apikey': apikey, 'daerah': daerah}).text
     api2 = _json_data_xenzi_(api1)
     if api2['message'] in 'jadwal sholat v2.0':
          print (f'\n {m}• {p}Info Jadwal Sholat V2.0')
          print (f' {m}• {p}Kota/daerah {m}: {h}{api2["city"]}')
          print (f' {m}• {p}Negara      {m}: {h}{api2["country"]}')
          print (f' {m}• {p}Waktu       {m}: {h}{api2["date"]}')
          print (f' {m}• {p}Fajar       {m}: {h}{api2["fajar"]}')
          print (f' {m}• {p}Shurooq     {m}: {h}{api2["shurooq"]}')
          print (f' {m}• {p}Dhurh       {m}: {h}{api2["dhuhur"]}')
          print (f' {m}• {p}Asar        {m}: {h}{api2["asar"]}')
          print (f' {m}• {p}Maghrib     {m}: {h}{api2["maghrib"]}')
          print (f' {m}• {p}Isya        {m}: {h}{api2["isya"]}')
          input (f' {m}• {l}[{p}Enter{l}]')
          Jadwal_Sholat()
     elif api2['message'] in 'apikey invalid':
          print (f' {m}• {p}apikey invalid')
     else:
          print (f' {m}• {p}daerah invalid')

if __name__ == '__main__':
    Jadwal_Sholat()
