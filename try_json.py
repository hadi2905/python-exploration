# -*- coding: UTF-8 -*-
"""
Beispiele für den Import von JSON-Dateien und das Arbeiten mit Posix-Timestamps
"""

import json
import datetime as dt
import math

def import_raspberry_mysql_data():
    """
    Liest die Export-Dateien der MySQL-Datenbank der web.de Homepage

    :return: nix
    """
    with open('/home/dieter/Family/KnowHow_PC_Software/Internet und WLAN/WEB.DE Hosting/Backup/export_tabelle_st_herkunft.json') as json_file:
        data = json.load(json_file)
        for e in data:
            print(e)


    with open('/home/dieter/Family/KnowHow_PC_Software/Internet und WLAN/WEB.DE Hosting/Backup/export_tabelle_messwert.json') as json_file:
        data = json.load(json_file)
        for e in data:
            print(e)

def import_journalctl_data(journal_file, example=0, arg1=None):
    """
    Verarbeitet eine JSON-Datei des journalctl
    Export des Journals vorher mit: journalctl -b -1 --system -o json > boot-1.json
    Jeder Journal-Eintrag bildet eine Zeile die mit {} geklammert ist, Da die Gesamtheit der Einträge nicht durch [] geklammert werden,
    läuft der JSON-Parser auf einen Fehler, wenn man versucht die Datei mit json.json_load als Ganzes zu verarbeiten.
    Vielmehr muss jede Zeile einzeln gelesen und mit json.json_loads interpretiert werden
    """
    with open(journal_file) as the_file:
        if example==0:
            # gibt alle Elemente der n-ten Zeile aus (n wird in arg1 übergeben)
            n = 0
            for line in the_file:
                n += 1
                obj = json.loads(line)
                if arg1 is None or arg1==n:
                    for k, el in obj.items():
                        print('{}:\t{}'.format(k, el))
                    # Die TIMESTAMPs sind auf die Mikrosekunde genau. Für die Umwandlung in ein DATETIME-Objekt müssen 6 Stellen abgeschnitten werden
                    t = dt.datetime.fromtimestamp(int(obj['__REALTIME_TIMESTAMP'][:-6]))
                    mt = dt.datetime.fromtimestamp(int(obj['__MONOTONIC_TIMESTAMP'][:-6]))
                    print('t={}\tmt={}'.format(t, mt))
                    break

        elif example==1:
            # liest alle Einträge ein; gibt von jedem n-ten Eintrag eine Ausgabe; rechnet mit Posix-Timestamps
            obj_list = []
            for line in the_file:
                obj_list.append(json.loads(line))
            print(len(obj_list))
            i = 0
            while i < len(obj_list):
                mt = int(obj_list[i]['__MONOTONIC_TIMESTAMP'][:-6])
                print("{:8}{:14}\t{}".format(i, mt, dt.datetime.fromtimestamp(mt)))
                i += 50

            try:
                t = dt.datetime.fromtimestamp(int(obj_list[0]['__REALTIME_TIMESTAMP'][:-6]))
                mt = dt.datetime.fromtimestamp(int(obj_list[0]['__MONOTONIC_TIMESTAMP'][:-6]))
                print('Zeile 1\tt={}\tmt={}'.format(t, mt))

                n = len(obj_list)-1
                t = dt.datetime.fromtimestamp(int(obj_list[n]['__REALTIME_TIMESTAMP'][:-6]))
                mt = dt.datetime.fromtimestamp(int(obj_list[n]['__MONOTONIC_TIMESTAMP'][:-6]))
                print('Zeile {}\tt={}\tmt={}'.format(n, t, mt))
            except:
                print("Fehler")
        elif example==2:
            # liest alle Einträge ein; schreibt uid, timestamp und message als Tupel in ein Dict mit monotonic_timestamp als Key
            msg = {}
            for line in the_file:
                el = json.loads(line)
                if '_UID' in el:
                    uid = int(el['_UID'])
                else:
                    uid = -1
                msg[int(el['__MONOTONIC_TIMESTAMP'])] = (uid, dt.datetime.fromtimestamp(int(el['__REALTIME_TIMESTAMP'][:-6])), el['MESSAGE'])

            n = 0
            for key, el in msg.items():
                n += 1
                print('{:5}\t{:8}\t{:8}\t{}\t\t{}'.format(n, round(key/1000000, 2), el[0], el[1], el[2]))

        elif example==3:
            # liest alle Einträge ein und schreibt sie in eine CSV-Datei
            journal_keys = []
            journal = []
            # zunächst nur die Keys identifizieren. (Die Einträge können unterschiedlich viele Keys haben!)
            for line in the_file:
                el = json.loads(line)
                journal.append(el)
                for k in el.keys():
                    if k not in journal_keys:
                        journal_keys.append(k)
            journal_keys.remove('__CURSOR')
            print(len(journal_keys), journal_keys)

            # jetzt CSV-Datei schreiben
            f = open('journal.csv', 'w')
            for k in journal_keys:
                f.write(k+';')
            f.write('\n')
            n = 0
            for el in journal:
                line = []
                for k in journal_keys:
                    if k in el:
                        if k=='__MONOTONIC_TIMESTAMP':
                            mt = dt.datetime.fromtimestamp(int(el[k][:-6]))
                            line.append(mt.strftime('%M:%S'))
                        elif k == '__REALTIME_TIMESTAMP':
                            mt = dt.datetime.fromtimestamp(int(el[k][:-6]))
                            line.append(mt.strftime('%y.%m.%d %H:%M:%S'))
                        else:
                            line.append(el[k])
                    else:
                        line.append('')
                for item in line:
                    try:
                        f.write('"'+item+'";')
                    except:
                        f.write('"Fehler in Eintrag {} TS {} MonoTS {} Msg {} Type {}"'.iormat(n, line[0], line[1], line[8], type(item)))
                f.write('\n')
                n += 1
            f.close()


if __name__=='__main__':
    #import_journalctl_data('/home/dieter/boot-1.json')
    #import_journalctl_data('/home/dieter/boot-2.json', 0, 1370)
    #import_journalctl_data('/home/dieter/boot-2.json', 2)
    #import_journalctl_data('/home/dieter/boot-2.json', 3)
    import_journalctl_data('journal_1905_verlangsamt.json', 3)
    #import_journalctl_data('/home/dieter/journal_haenger.json', 1)
