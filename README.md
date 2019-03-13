# DatabaseProsjekt

https://sqlitebrowser.org/ vil jeg tro funker fint på mac og windows for å se inni et databasefilen(trening3.db) med et grafisk grensesnitt. 
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
sqlite3 trening.db < test_db.sql
```
Begge sql filene må kjøres først for å initalisere prosjektet.

App.py er der jeg har startet, gui_test.py er kun testing av Tkinter
Har nå mulighet legge inn person i databasen og finne person fra personnr i databasen. 

