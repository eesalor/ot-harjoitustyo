# Ohjelmistotekniikka, harjoitustyö

Tavoitteena on toteuttaa omavalintainen **ohjelmisto** ns. **työpöytäsovelluksena**. Alustava idea on toteuttaa jonkinlainen tehtävienhallintaan tai kirjanpitoon liittyvä sovellus.

 *Sovelluksen aihe tarkentuu myöhemmin.*

[laskarit](https://github.com/eesalor/ot-harjoitustyo/tree/main/laskarit)

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/eesalor/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/eesalor/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [Muutosloki (changelog)](https://github.com/eesalor/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)


## Sovelluksen asennus

1. Kopioi Git-projekti omalle koneellesi:
```
$ git clone https://github.com/eesalor/ot-harjoitustyo.git
```

2. Siirry projektikansioon ja asenna projektin riippuvuudet Poetrylla:
```
$ poetry install
```
- Huom. Jos asennuksessa tulee alla oleva virhe, suorita komento `poetry lock` ja sen jälkeen asenna uudelleen `poetry install`.

  - ```pyproject.toml changed significantly since poetry.lock was last generated. Run 'poetry lock' to fix the lock file```


3. Alusta tietokanta:
```
$ poetry run invoke init-database
```
4. Käynnistä sovellus:
```
$ poetry run invoke start
```
