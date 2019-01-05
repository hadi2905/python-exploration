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

def import_journalctl_data(journal_file, example=0):
    """
    Verarbeitet eine JSON-Datei des journalctl
    Export des Journals vorher mit: journalctl -b -1 --system -o json > boot-1.json
    Jeder Journal-Eintrag bildet eine Zeile die mit {} geklammert ist, Da die Gesamtheit der Einträge nicht durch [] geklammert werden,
    läuft der JSON-Parser auf einen Fehler, wenn man versucht die Datei mit json.json_load als Ganzes zu verarbeiten.
    Vielmehr muss jede Zeile einzeln gelesen und mit json.json_loads interpretiert werden
    """
    with open(journal_file) as the_file:
        if example==0:
            for line in the_file:
                obj = json.loads(line)
                for k, el in obj.items():
                    print('{}:\t{}'.format(k, el))
                break
        elif example==1:
            obj_list = []
            for line in the_file:
                obj_list.append(json.loads(line))
            print(len(obj_list))
            i = 0
            while i < len(obj_list):
                print("{}\t\t{}".format(i, obj_list[i]['__MONOTONIC_TIMESTAMP']))
                i += 50

if __name__=='__main__':
    #import_journalctl_data('/home/dieter/boot-1.json')
    #import_journalctl_data('/home/dieter/boot-1.json', 1)
    import_journalctl_data('/home/dieter/journal_haenger.json', 1)