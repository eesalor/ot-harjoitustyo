# Muutosloki (changelog)

## Viikko 3
- Käyttäjä voi lisätä uusia tehtäviä sovellukseen. Tässä vaiheessa tehtävä sisältää vain sanallisen kuvauksen.
- Käyttäjä näkee sovellukseen lisätyt tehtävät.
- Sovellus sisältää aloitusikkunan ja näkymän, jossa käyttäjä voi lisätä lomakkeen kautta tehtäviä ja nähdä kaikki lisätyt tehtävät.
- Sovellukseen on lisätty luokka Task, joka määrittelee tehtävään liittyvät attribuutit. 
- Sovellukseen on lisätty sovelluslogiikkaa hoitava TaskService-luokka.
- Sovellukseen on lisätty tehtävien tallennuksesta SQL-tietokantaan huolehtiva TaskRepository-luokka.
- Sovellusta on testattu, että TaskRepository-luokka lisää uuden tehtävän ja palauttaa kaikki sovellukseen lisätyt tehtävät.
