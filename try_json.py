import json

with open('/home/dieter/Family/KnowHow_PC_Software/Internet und WLAN/WEB.DE Hosting/Backup/export_tabelle_st_herkunft.json') as json_file:
    data = json.load(json_file)
    for e in data:
        print(e)


with open('/home/dieter/Family/KnowHow_PC_Software/Internet und WLAN/WEB.DE Hosting/Backup/export_tabelle_messwert.json') as json_file:
    data = json.load(json_file)
    for e in data:
        print(e)
