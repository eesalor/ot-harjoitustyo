# Testausdokumentti

Sovelluksen testaamisen osalta on suoritettu yksikkö- ja integraatiotestausta sekä järjestelmätestausta. Yksikkö- ja integraatiotesteissä on käytetty automatisoituja testejä, kun taas järjestelmätestaus on suoritettu manuaalisesti käyttöliittymän kautta.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka
Testiluokan ![TestTaskService](/src/tests/task_service_test.py) avulla testataan sovelluslogiikasta vastaavaa `TaskService`-luokkaa. Testiluokassa muodostetaan luokan `TaskService` olio. 
Tehtävien ja kategorioiden tietokantaoperaatiosta vastaavista luokista `TaskRepository` ja `CategoryRepository` muodostetut oliot annetaan riippuvuutena kyseiselle `TaskService`-luokan oliolle.
Testaamisessa käytetään testitietokantatiedostoa `test_database.db`.

### Repositorio-luokat

Sovelluksen tietokantaoperaatioista vastaavien luokan `TaskRepository` testaamisessa käytetään testiluokkaa ![TestTaskRepository](/src/tests/task_repository_test.py)
ja luokan `CategoryRepository` osalta ![TestCategoryRepository](/src/tests/category_repository_test.py)-luokkaa.

Näiden repositorio-luokkien testaamisessa käytetään testitietokantatiedostoa `test_database.db`, joka on määritelty konfiguraatiotiedostossa ![.env.test](/.env.test).

### Testauskattavuus

Sovelluksen testauskattavuus on 98 %. Käyttöliittymän testaaminen on jätetty testauskattavuuden laskemisen ulkopuolelle.

![](/dokumentaatio/kuvat/testikattavuus.png)

Testauskattavuuden laskemiseen mukaan otettavat tiedostot on määritelty tiedostossa ![.coveragerc](/.coveragerc), joka sijaitsee projektin juuressa. Testauksen kohdekansioksi on määritelty *src*.
Lisäksi on määritelty, että testauskattavuuden laskemisen ulkopuolelle jätetään
- Käyttöliittymään liittyvät tiedostot, jotka sijaitsevat hakemistossa *ui*
- Testitiedostot, jotka sijaitsevat hakemistossa *tests*
- `__init__.py`-tiedostot
- Pääohjelman sisältävä `index.py`

Testiraportin perusteella tiedostoja *config.py* ja *initialize_database.py* ei testattu.
Sovelluksen päätoiminnallisuudet eli tehtäviin liittyvät toiminnot testattiin monipuolisesti erilaisilla testitapauksilla.

## Järjestelmätestaus

Sovelluksen toimivuutta testattiin myös manuaalisella järjestelmätestauksella, jossa testattiin sovelluksen asentamista, kofigurointia sekä sovellukselle määriteltyjä toiminnallisuusvaatimuksia käyttöliittymän kautta.

### Sovelluksen asennus ja konfigurointi

Sovelluksen ![käyttöohjeessa](/dokumentaatio/kayttoohje.md) sisältää ohjeet sovelluksen asentamiseen, konfiguroimiseen sekä sovelluksen käyttämiseen.
Sovellusta on näiden ohjeiden perusteella kokeiltu asentaa ja testata Linux-ympäristössä käyttäen Pythonin versiota 3.12. Sovelluksen konfiguraatiotiedostossa ![.env](/.env) määriteltyä tietokantatiedoston nimeä on kokeiltu vaihtaa ja testata sovelluksen toimintaa. Sovelluksen eri käyttötilanteet on käyty läpi.

### Toiminnallisuudet

Sovellukseen toteutetut toiminnallisuudet on kuvattu projektin ![vaatimusmäärittelyssä](/dokumentaatio/vaatimusmaarittely.md).
Järjestelmää on testattu näiden toiminnallisuuksien osalta. Sovelluksen toimintaa on testattu erilaisilla syötteillä. Esimerkiksi tehtävän lisäämisessä kokeiltiin lisätä tehtävää tyhjällä tai liian pitkillä syötteillä.
Tehtävän määräajan osalta kokeiltiin myös tyhjää tai väärässä muodssa olevaa syötettä sekä mennyttä päivämäärää. Virheelliset syötteet tuottivat käyttöliittymään oikeanlaiset virheilmoitukset.

Tehtävien poistamisen ja tehdyksi / tekemättömäksi merkitsemisen osalta testattiin, että toiminnallisuudet kohdistuvat oikeisiin tehtäviin. Lisäksi testattiin,
että tekemättömiä tehtäviä voi poistaa tai merkitä tehdyksi vain niihin tarkoitetuilla painikkeilla. Vastaavaa testattiin myös tehdyiksi merkittyjen tehtävien osalta.
