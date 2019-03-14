# DatabaseProsjekt

https://sqlitebrowser.org/ vil jeg tro funker fint på mac og windows for å se inni et databasefilen med et grafisk grensesnitt. 
Jeg vil anbefale å bruke terminalen hvis man bruker Mac eller linux.

For Mac og tildels linux

```bash
brew install sqlite3
cd <mappe hvor du har filen>/trening3.db
sqlite3 trening.db
```
Det vil åpne en prompt med full tilgang til databasen
hvis du vil kjøre det som ligger i .sql filene

```bash
sqlite3 trening3.db < test_db.sql
```
Begge sql filene må kjøres først for å initalisere prosjektet.

For øyeblikket er navnet på databasen hardkodet i prosjektet under konstanten
TRENINGSDB, så gjerne lag en db fil som heter "trening3.db"

App.py og okt.py  er der jeg har startet 
Kjør gui_test.py for å se GUI
```bash
pyhon3 gui_test.py
```

Ideen vil være å gi kun  primary key hentes objektet fra databasen, med ekstra
argumenter lages det et entry i databasen.

DB klassen vil ha mange abstrakte funksjoner

