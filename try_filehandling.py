try:
    with open('log_trial.py','r') as my_file:
        for line in my_file:
            print(line)
except FileNotFoundError:
    print('Kann datei nicht öffnen')
finally:
    print('Diese Meldung kommt auf jeden Fall')
