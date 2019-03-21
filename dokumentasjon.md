# tables

tables er en mappe med en pythonfil for noen av tabellene i databasen vår. Hvert
klasse instansieres enten ved å gi en primary key, eller å gi alle feltene som
tabellen trenger. Da vil objektet enten hentes ut fra databasen eller
skapes. Klassene har en save() funksjon som legger objektet inn i databasen.

# database.py

Database.py inneholder en abstrakt klasse DB som har mange abstrakte funksjoner
som er praktiske for å snakke med databasen. Det er mer eller mindre alle
funksjoner som snakker med databasen unntatt save() funksjonene i tabellklassen. 

# Use cases
  * Registrere apparater, øvelser og treningsøkter

    Dette gjøres enkelt fra brukergrensesnittet vårt. Her lages det apparat,
    ovelse og treningsokt instanser som lagres i databasen. 
  
  * Få opp informasjon om et antall n sist gjennomførte trenignsøkter med
      notater, der n spesifiseres av brukeren 

      Dette gjøres også enkel fra brukergrensesnittet, se get_n_treningsokter()
      fra database.py for SQL-spørringen
  
  * For hver enkelt øvelse skal det være mulig å se en resultatlogg i et gitt
      tidsintervall spesifisert av brukeren.
      
      Se brukergrensesnittet og database.py for implementasjon
      
  * Lage øvelsesgrupper og finne øvelser som er i samme gruppe

    Se brukergrensesnitt
  
  * Se personlig rekord for en øvelse

    Definerer personlig rekord som MAX(antall_kilo * antall_set). Ovelser uten
    apparat returnerer kun beskrivelsen og navn
