import json

def import_raspberry_mysql_data():
    with open('/home/dieter/Family/KnowHow_PC_Software/Internet und WLAN/WEB.DE Hosting/Backup/export_tabelle_st_herkunft.json') as json_file:
        data = json.load(json_file)
        for e in data:
            print(e)


    with open('/home/dieter/Family/KnowHow_PC_Software/Internet und WLAN/WEB.DE Hosting/Backup/export_tabelle_messwert.json') as json_file:
        data = json.load(json_file)
        for e in data:
            print(e)

def import_journalctl_data(journal_file):
    """
    Verarbeitet eine JSON-Datei des journalctl
    Export des Journals vorher mit: journalctl -b -1 --system -o json > boot-1.json
    Jeder Journal-Eintrag bildet eine Zeile die mit {} geklammert ist, Da die Gesamtheit der Einträge nicht durch [] geklammert werden,
    läuft der JSON-Parser auf einen Fehler, wenn man versucht die Datei mit json.json_load als Ganzes zu verarbeiten.
    Vielmehr muss jede Zeile einzeln gelesen und mit json.json_loads interpretiert werden
    """
    with open(journal_file) as the_file:
        for line in the_file:
            obj = json.loads(line)
            print(obj)
            for k, el in obj.items():
                print('{}:\t{}'.format(k, el))
            break

if __name__=='__main__':
    import_journalctl_data('/home/dieter/boot-1.json')
    #import_journalctl_data('/home/dieter/journal_haenger3.json')