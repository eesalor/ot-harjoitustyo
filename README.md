# Manage Your Tasks

Sovelluksen tarkoituksena on, että käyttäjä voi pitää kirjaa ja hallita tekemättömiä tehtäviään. Sovellusta on mahdollista käyttää yksi käyttäjä. Sovellus toteutetaan työpöytäsovelluksena, joka hyödyntää SQL-tietokantaa.

Sovellus on ohjelmistotekniikan harjoitustyö.

## Versiot

- Sovelluksen viimeisin GitHub release: [viikko6](https://github.com/eesalor/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio

- [Käyttöohje](https://github.com/eesalor/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/eesalor/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Sovelluksen arkkitehtuuri](https://github.com/eesalor/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](https://github.com/eesalor/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [Muutosloki (changelog)](https://github.com/eesalor/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)


## Sovelluksen asennus

1. Kopioi Git-projekti omalle koneellesi:
```
git clone https://github.com/eesalor/ot-harjoitustyo.git
```

2. Siirry projektikansioon ja asenna projektin riippuvuudet Poetrylla:
```
poetry install
```
- Huom. Jos asennuksessa tulee alla oleva virhe, suorita komento `poetry lock` ja sen jälkeen asenna uudelleen `poetry install`.

  - ```pyproject.toml changed significantly since poetry.lock was last generated. Run 'poetry lock' to fix the lock file```


3. Alusta tietokanta:
```
poetry run invoke init-database
```
4. Käynnistä sovellus:
```
poetry run invoke start
```

## Komentorivillä suoritettavia komentoja

**Tietokannan alustaminen**

Komento alustaa SQL-tietokannan. Komennon suorittaminen korvaa mahdollisen olemassa olevan tietokannan.
```
poetry run invoke init-database
```

**Sovelluksen käynnistäminen**
```
poetry run invoke start
```

**Testien suorittaminen**
```
poetry run invoke test
```

**Testikattavuusraportin tuottaminen**
```
poetry run invoke coverage-report
```

**Koodin laadun tarkistaminen**

Komento suorittaa koodin laadun tarkistuksen hyödyntämällä Pylint-työkalua. Laadun tarkistus tehdään [.pylintrc](https://github.com/eesalor/ot-harjoitustyo/blob/main/.pylintrc)-tiedoston sisältämien sääntöjen perusteella.
```
poetry run invoke lint
```
