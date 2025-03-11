#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import requests
import json
import html

link = "https://fahrplan.oebb.at/bin/stboard.exe/dn?L=vs_scotty.vs_liveticker&evaId=8102059&boardType=dep&productsFilter=1011111111011&dirInput=&tickerID=dep&start=yes&eqstops=false&showJourneys=20&additionalTime=0&outputMode=tickerDataOnly"
data = requests.get(link)
dataJson = y = json.loads(data.text[14:])

now = datetime.now()
now = now.strftime("%d.%m.%y %H:%M")
 
img = Image.new('L', (800, 600), color = (255))
fnt = ImageFont.truetype('/usr/share/fonts/truetype/arial.ttf', 30)
d = ImageDraw.Draw(img)

d.text((20,10), "Tullnerfeld - Abfahrten", font=fnt, fill=(0))
d.text((580,10), now, font=fnt, fill=(0))

d.text((20,60), "Zeit", font=fnt, fill=(0))
d.text((120,60), "Aktuell", font=fnt, fill=(0))
d.text((240,60), "Zug", font=fnt, fill=(0))
d.text((360,60), "Nach", font=fnt, fill=(0))
d.text((720,60), "Steig", font=fnt, fill=(0))


line = 2
for journey in dataJson['journey']:
    if (journey['pr'][:3] != "Bus"):
        d.text((20,50*line+10), journey['ti'], font=fnt, fill=(0))
        if (journey['rt']):
            d.text((120,50*line+10), journey['rt']['dlt'], font=fnt, fill=(0))
        d.text((240,50*line+10), journey['pr'], font=fnt, fill=(0))
        d.text((360,50*line+10), html.unescape(journey['st'])[:23], font=fnt, fill=(0))
        d.text((720,50*line+10), journey['tr'], font=fnt, fill=(0))
        line += 1    

img.save('/var/www/html/oebb/90grad.png')
img = img.rotate(90, expand=True)
img.save('/var/www/html/oebb/status.png')