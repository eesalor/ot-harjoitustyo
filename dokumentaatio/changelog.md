# Muutosloki (changelog)

## Viikko 3
- Käyttäjä voi lisätä uusia tehtäviä sovellukseen. Tässä vaiheessa tehtävä sisältää vain sanallisen kuvauksen.
- Käyttäjä näkee sovellukseen lisätyt tehtävät.
- Sovellus sisältää aloitusikkunan ja näkymän, jossa käyttäjä voi lisätä lomakkeen kautta tehtäviä ja nähdä kaikki lisätyt tehtävät.
- Sovellukseen on lisätty luokka Task, joka määrittelee tehtävään liittyvät attribuutit. 
- Sovellukseen on lisätty sovelluslogiikkaa hoitava TaskService-luokka.
- Sovellukseen on lisätty tehtävien tallennuksesta SQL-tietokantaan huolehtiva TaskRepository-luokka.
- Sovellusta on testattu, että TaskRepository-luokka lisää uuden tehtävän ja palauttaa kaikki sovellukseen lisätyt tehtävät.

## Viikko 4
- Käyttäjä voi lisätä tehtävään myös deadlinen.
- Käyttäjä voi poistaa lisäämiään tehtäviä.
- Sovellusta on testattu, että TaskRepository-luokka poistaa tehtävän.
- Sovellusta on testattu, että TaskService-luokka lisää uuden tehtävän, palauttaa sovellukseen lisätyt tehtävät ja poistaa tehtäviä.
- Sovellukseen on lisätty Pylint-työkalu koodin laadun tarkistamiseksi.

## Viikko 5
- Käyttäjä voi merkitä tekemättömän tehtävän tehdyksi ja tehdyn tehtävän tekemättömäksi.
- Käyttäjä näkee tekemättömät ja tehdyt tehtävät erillisissä luetteloruuduissa.
- Käyttäjä voi poistaa sekä tekemättömiä että tehtyjä tehtäviä.
- Sovellusta on testattu, että TaskReporitory-luokka merkitsee tehtävät tehdyksi/tekemättömäksi.
- Sovellusta on testattu, että TaskRepository-luokka hakee tekemättömät ja tehdyt tehtävät.

## Viikko 6
- Käyttäjä voi lisätä tehtävään kategorian luodessaan uutta tehtävää.
- Käyttäjä voi poistaa lisäämiään kategorioita.
- Sovellusta on testattu, että TaskService-luokka merkitsee tehtäviä tehdyksi/tekemättömäksi.
- Sovellusta on testattu, että CategoryRepository-luokka lisää kategorian, hakee kategorioita ja poistaa kategorian.
- Sovellusta on testattu, että TaskRepository-luokka lisää tehtäviin kategorian ja hakee tiedon tehtävän kategoriasta.
