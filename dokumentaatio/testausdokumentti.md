# Testausdokumentti

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka
Testiluokan ![TestTaskService](/src/tests/task_service_test.py) avulla testattiin sovelluslogiikasta vastaavaa `TaskService`-luokkaa. 

### Repositorio-luokat

Sovelluksen tietokantaoperaatioista vastaavien luokan `TaskRepository` testaamisessa käytettiin testiluokkaa ![TestTaskRepository](/src/tests/task_repository_test.py)
ja luokan `CategoryRepository` osalta ![TestCategoryRepository](/src/tests/category_repository_test.py)-luokkaa.

Näiden repositorio-luokkien testaamisessa käytetään testitietokantatiedostoa `test_database.db`, joka on määritelty konfiguraatiotiedostossa ![.env.test](/.env.test).

### Testauskattavuus

Sovelluksen testauskattavuus on 98 %. Käyttöliittymän testaaminen on jätetty testauskattavuuden laskemisen ulkopuolelle.

Projektin juuressa tiedossa ![.coveragerc](/.coveragerc) on määritelty testauksen kohdekansio *src* ja tiedostot, joita ei lasketa mukaan testikattavuuden laskemisessa.
Esimerkiksi hakemistossa *ui* sijaitsevia käyttöliittymän tiedostoja, hakemistossa *tests* sijaitsevia testitiedostoja, `__init__.py`-tiedostoja eikä pääohjelman sisältävää `index.py` oteta mukaan.



Testiraportin perusteella tiedostoja *config.py* ja *initialize_database.py* ei testattu.

## Järjestelmätestaus

Sovelluksen toimivuutta testattiin myös manuaalisella järjestelmätestauksella, jossa testattiin sovelluksen asentamista, kofigurointia sekä sovellukselle määriteltyjä toiminnallisuusvaatimuksia käyttöliittymän kautta.

### Sovelluksen asennus ja konfigurointi


### Toiminnallisuudet

Sovellukseen toteutetut toiminnallisuudet on kuvattu projektin ![vaatimusmäärittelyssä](/dokumentaatio/vaatimusmaarittely.md).
Järjestelmää on testattu näiden toiminnallisuuksien osalta. Sovelluksen toimintaa on testattu erilaisilla syötteillä. Esimerkiksi tehtävän lisäämisessä kokeiltiin lisätä tehtävää tyhjällä tai liian pitkillä syötteillä.
Tehtävän määräajan osalta kokeiltiin myös tyhjää tai väärässä muodssa olevaa syötettä sekä mennyttä päivämäärää. Virheelliset syötteet tuottivat käyttöliittymään oikeanlaiset virheilmoitukset.

Tehtävien poistamisen ja tehdyksi / tekemättömäksi merkitsemisen osalta testattiin, että toiminnallisuudet kohdistuvat oikeisiin tehtäviin. Lisäksi testattiin,
että tekemättömiä tehtäviä voi poistaa tai merkitä tehdyksi vain niihin tarkoitetuilla painikkeilla. Vastaavaa testattiin myös tehdyiksi merkittyjen tehtävien osalta.
