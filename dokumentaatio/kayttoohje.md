# Käyttöohje

## Sovelluksen lataaminen

Manage Your Tasks -sovelluksen julkaistut versiot eli releaset löydät ![täältä](https://github.com/eesalor/ot-harjoitustyo/releases).

Lataa uusimman releasen lähdekoodi (*Source code*) kohdan *Assets* alta, kuten on havainnollistettu alla olevassa kuvassa.

![](/dokumentaatio/kuvat/kayttoohje_lataus.png)

## Konfigurointi

Sovelluksen käyttämän tietokantatiedoston nimi ja sijainti määritellään tiedostossa ![.env](https://github.com/eesalor/ot-harjoitustyo/blob/main/.env).

## Sovelluksen käynnistäminen

Sovelluksen riippuvuudet asennetaan komennolla
```
poetry install
```
Sovelluksen tietokanta alustetaan ennen käynnistämistä komennolla
```
poetry run invoke init-database
```
Sovelluksen voi käynnistää komennolla
```
poetry run invoke start
```

## Käynnistyminen / aloitusnäkymä

Sovelluksen käynnistämisen jälkeen ilmestyy ensin aloitusnäkymä.

Sovelluksen päänäkymään eli tehtävänäkymään pääsee painamalla nappia ”Start”.

![](/dokumentaatio/kuvat/kayttoohje_aloitus.png)

## Tehtävänäkymä

Tehtävänäkymässä voi

- luoda uusia tehtäviä
- luoda uusia kategorioita
- merkitä tehtäviä tehdyksi / tekemättömäksi
- poistaa tehtäviä
- poistaa kategorioita

Alla on kuvattu näitä toiminnallisuuksia tarkemmin.

### Uuden tehtävän luominen

Sovelluksessa on mahdollista lisätä uusia tehtäviä ja niihin liittyviä määräaikoja. Molemmat ovat pakollisia tietoja. Lisäksi tehtävään voi halutessaan lisätä kategorian.

Kenttään ”Task” kirjoitetaan tehtävän nimi, jonka enimmäispituus on 100 merkkiä. Kenttään ”Date” kirjoitetaan määräaika muodossa ”pp.kk.vvvv”. Lisättävä päivämäärä ei voi olla mennyt päivämäärä.
Kategoriakenttään ”Enter or select category” voi kirjoittaa kategorian tai valita valikosta aiemmin lisätyn kategorian. Jos kategoriaa ei lisätä, tehtävään tulee näkyviin "(No category)".

Tehtävä luodaan painamalla nappia ”Create task”.

![](/dokumentaatio/kuvat/kayttoohje_uusi_tehtava_1.png)

Mikäli tehtävän luominen onnistuu, lisätty tehtävä siirtyy luetteloruutuun ”Uncompleted tasks”.

![](/dokumentaatio/kuvat/kayttoohje_uusi_tehtava_2.png)

### Uuden kategorian luominen

Uuden kategorian lisääminen on mahdollista vain tehtävän lisäämisen yhteydessä, kuten on kuvattu edellisessä kohdassa. Erillistä toimintoa pelkän kategorian lisäämiselle ei ole.

Kun tehtävän lisäämisen yhteydessä kategoriakenttään syötetään uusi kategoria, se tallennetaan sovelluksen tietokantaan. Seuraavaa tehtävää luodessa käyttäjän on mahdollista valita pudotusvalikosta jokin aiemmin luoduista kategorioista.

![](/dokumentaatio/kuvat/kayttoohje_kategorian_valinta.png)

### Tehtävien merkitseminen tehdyksi / tekemättömäksi

Oletuksena uuden tehtävän tila on tekemätön (uncompleted). Sovelluksessa on mahdollista merkitä tekemätön tehtävä tehdyksi valitsemalla kyseinen tehtävä luettelosta ja painamalla kyseisen luetteloruudun alapuolella olevaa nappia ”Set completed”.

![](/dokumentaatio/kuvat/kayttoohje_uusi_tehtava_2.png)

Tämän jälkeen tehtävä siirtyy viereiseen luetteloon, jossa näkyy tehdyiksi merkityt tehtävät (”Completed tasks”).

![](/dokumentaatio/kuvat/kayttoohje_tehtava_tehdyksi.png)

Sovelluksessa voi myös vastaavasti muuttaa tehtyjen tehtävien tilan takaisin tekemättömäksi valitsemalla luettelosta "Completed tasks" kyseinen valmiiksi merkitty tehtävä ja painamalla kyseisen luettelon alapuolella olevaa nappia ”Set uncompleted”. Tämän jälkeen tehtävä siirtyy takaisin viereiseen luetteloon, jossa näkyy tekemättömät tehtävät (”Uncompleted tasks”).

### Tehtävien poistaminen

Sovelluksessa on mahdollista poistaa sekä tekemättömiä että tehtyjä tehtäviä.
Tekemättömien tehtävien poistaminen tapahtuu valitsemalla luettelosta tehtävän ja painamalla kyseisen luettelon alla olevaa nappia ”Delete selected task”, minkä jälkeen tehtävä poistuu luettelosta.

Vastaavasti tehtyjen tehtävien poistaminen tapahtuu valitsemalla luettelosta tehtävän ja painamalla kyseisen luettelon alla olevaa nappia ”Delete selected task”.

### Kategorian poistaminen

Sovellukseen lisättyjä kategorioita voi poistaa valitsemalla pudotusvalikosta poistettavan kategorian ja painamalla nappia ”Delete selected category”.

![](/dokumentaatio/kuvat/kayttoohje_kategorian_poisto_1.png)

Kategorian poistaminen poistaa kategorian myös niistä tehtävistä, joihin kyseinen kategoria on lisätty. Tällöin tehtävien kategorian osalta tulee näkyviin "(No category)".

![](/dokumentaatio/kuvat/kayttoohje_kategorian_poisto_2.png)
