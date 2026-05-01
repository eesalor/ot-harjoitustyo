# Sovelluksen arkkitehtuuri

## Rakenne

Sovelluksen arkkitehtuurityylinä on käytetty kerrosarkkitehtuuria. Sovellus on jaettu kolmeen kerrokseen: Ylimmässä kerroksessa on käyttöliittymän koodi, toisessa kerroksessa on sovelluslogiikan koodi ja kolmannessa kerroksessa on tietojen tallennukseen liittyvä koodi.

Alla olevassa pakkauskaaviossa havainnollistetaan sovelluksen hakemistorakennetta sisältäen pakkaukset käyttöliittymästä *ui*, sovelluslogiikasta *services* ja tietojen tallennuksesta *repositories*. Lisäksi sovelluksen tietokohteet sisältyvät pakkaukseen *entities.*

 ![Pakkauskaavio arkkitehtuurista](/dokumentaatio/kuvat/pakkauskaavio_arkkitehtuuri.png)

## Käyttöliittymä

Sovelluksen käyttöliittymässä on kaksi näkymää: aloitusnäkymä ja tehtävänäkymä.

Tehtävänäkymä on sovelluksen päänäkymä, jonka kautta sovelluksen sisältämiä päätoimintoja voidaan käyttää.

Aloitusnäkymästä vastaa ![StartView](https://github.com/eesalor/ot-harjoitustyo/blob/main/src/ui/start_view.py)-luokka. Tehtävänäkymä määritellään ![TaskView](https://github.com/eesalor/ot-harjoitustyo/blob/main/src/ui/task_view.py)-luokassa. Eri näkymien näyttämisestä vastaa luokka ![UI](https://github.com/eesalor/ot-harjoitustyo/blob/main/src/ui/ui.py).

## Sovelluslogiikka

Oheisessa luokkakaaviossa on kuvattu sovelluksen tietokohteita määrittävät luokat, niiden välinen suhde sekä luokkien sisältämät attribuutit. Luokassa ![Task](https://github.com/eesalor/ot-harjoitustyo/blob/main/src/entities/task.py) määritellään sovellukseen lisättävien tehtävien rakenne ja luokassa ![Category](https://github.com/eesalor/ot-harjoitustyo/blob/main/src/entities/category.py) kategorioiden rakenne. Yhteen tehtävään voi liittyä enintään yksi kategoria, mutta yksi kategoria voi liittyä useampaan tehtävään.

```mermaid
 classDiagram
    Task "*" -- "0..1" Category
    class Task{
        title
        date
        completed
        category
    }
    class Category{
        title
    }
```
Luokasta ![TaskService](https://github.com/eesalor/ot-harjoitustyo/blob/main/src/services/task_service.py) muodostettavan olion tehtävänä on sovelluksen toiminnallisuudet, kuten tehtävien lisääminen, merkitseminen tehdyksi ja poistaminen.

Esimerkkejä TaskService-luokan metodeista, joita käyttöliittymän eri toiminnoissa käytetään:
* `create_task(title, date, category)`
* `set_completed(task_id)`
* `delete_task(task_id)`

Sovelluslogiikasta vastaava palvelu *TaskService* käsittelee tehtäviä ja kategorioita luokkien ![TaskRepository](https://github.com/eesalor/ot-harjoitustyo/blob/main/src/repositories/task_repository.py) ja ![CategoryRepository](https://github.com/eesalor/ot-harjoitustyo/blob/main/src/repositories/category_repository.py) avulla. Luokat sijaitsevat hakemistossa *repositories*.

![Pakkauskaavio arkkitehtuurista](/dokumentaatio/kuvat/pakkauskaavio_arkkitehtuuri_luokilla.png)

## Tietojen tallennus

*Repositories* on tietojen tallennuksesta huolehtiva kerros. Luokka `TaskRepository` vastaa tehtävien tallentamisesta ja luokka `CategoryRepository` kategorioiden tallentamisesta. Molemmat luokat tallentavat tietoja SQLite-tietokantaan.

### Tiedostot

Sovellus tallentaa tehtäviä ja kategorioita SQLite-tietokantatauluihin. Tiedosto määritellään konfiguraatiotiedostossa ![.env](https://github.com/eesalor/ot-harjoitustyo/blob/main/.env). Tehtävät tallennetaan tauluun `Tasks`, joka sisältää tehtävän `id`-numeron, tehtävän kuvauksen `title`, tehtävän tilan `completed` (0=tekemättä, 1 = tehty) sekä kategorian id-numeron `category_id`.

Kategoriat tallennetaan tauluun `Categories` sisältäen kategorian `id`-numeron ja kategorian kuvauksen `title`.

Taulussa `Tasks` jokaisen tehtävän kohdalla on viittaus tehtävän kategoriaan `category_id`:n kautta, mikäli tehtävään on lisätty tieto kategoriasta.

## Sovelluksen päätoiminnallisuudet

### Tehtävän lisääminen ilman kategoriaa
Käyttäjä voi lisätä uuden tehtävän ollessaan sovelluksen päänäkymässä eli tehtävänäkymässä. Käyttäjä voi syöttää tekstikenttiin tehtävän kuvauksen ja määräajan ja lisätä uuden tehtävän painamalla "Create"-nappia. Oletuksena tehtävän tila on tekemätön. Tehtävän otsikko, määräaika ja tila tallennetaan SQL-tietokantatauluun. Lisätty tehtävä ilmestyy lopulta tehtävänäkymässä olevaan luetteloruutuun. Alla olevassa sekvenssikaaviossa on kuvattu sovelluksen toiminta pääpiirteittäin kyseisen käyttötapauksen osalta:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant TaskService
  participant TaskRepository
  participant CategoryRepository
  participant task
  participant Database@{ "type" : "database" }

  User->>UI: enter title: "Finalize your project"
  User->>UI: enter date: "10.05.2026"
  User->>UI: click "Create" button
  UI->>TaskService: create_task("Finalize your project", "10.05.2026", category=None)
  TaskService->>task: Task("Finalize your project", "10.05.2026")
  TaskService->>TaskRepository: create_task(task, category_id=None)
  TaskRepository->>Database: INSERT INTO Tasks (title, date, completed) <br/>VALUES (task.title, task.date, 0);
  Database-->>TaskRepository:
  TaskRepository-->>TaskService:
  TaskService-->>UI:
  UI->>UI: update_task_view()
  UI->>UI: show_task_view()
```
Kun käyttäjä painaa "Create"-nappia, niin tapahtumakäsittelijä kutsuu sovelluslogiikan metodia `create_task`. Parametreiksi annetaan tehtävän kuvaus (`title`), määräaika (`date`) ja kategoria (`category`). 

Sovelluslogiikan metodissa `create_task` tarkistetaan, onko parametrina annettu kategoriaa. Tässä käyttötapauksessa kategoriaa ei ole. Kyseinen metodi kutsuu edelleen luokan `TaskRepository` metodia `create_task`, joka lisää tehtävän tiedot tietokantaan. Lopuksi kutsutaan käyttöliittymän `UI` metodia `_update_task_view`, joka kutsuu metodia `show_task_view`. Tämän seurauksena käyttöliittymän näkymä `TaskView` päivitetään, jolloin uusi tehtävä ilmestyy näkyviin tehtävälistaan.


### Tehtävän lisääminen sisältäen kategorian

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant TaskService
  participant TaskRepository
  participant CategoryRepository
  participant category
  participant task
  participant Database@{ "type" : "database" }

  User->>UI: enter title: "Finalize your project"
  User->>UI: enter date: "10.05.2026"
  User->>UI: enter category: "Studies"
  User->>UI: click "Create" button
  UI->>TaskService: create_task("Finalize your project", "10.05.2026", "Studies")
  TaskService->>TaskService: create_category("Studies")
  TaskService->>category: Category("Studies")
  TaskService->>CategoryRepository: find_category_by_name("Studies")
  CategoryRepository-->>TaskService: return False
  TaskService->>CategoryRepository: create_category(category)
  CategoryRepository->>Database: INSERT INTO Categories (title) <br>VALUES (category.title);
  Database-->>CategoryRepository:
  CategoryRepository-->>TaskService:
  TaskService->>CategoryRepository: get_category_id("Studies")
  CategoryRepository-->>TaskService: return "1"
  TaskService->>task: Task("Finalize your project", "10.05.2026")
  TaskService->>TaskRepository: create_task(task, category_id=1)
  TaskRepository->>Database: INSERT INTO Tasks (title, date, category_id, completed) <br/>VALUES (task.title, task.date, category_id, 0);
  Database-->>TaskRepository:
  TaskRepository-->>TaskService:
  TaskService-->>UI:
  UI->>UI: update_task_view()
  UI->>UI: show_task_view()
```

### Tehtävän merkitseminen tehdyksi
Käyttäjä voi merkitä tehtävän tehdyksi ollessaan sovelluksen päänäkymässä eli tehtävänäkymässä. Käyttäjä voi valita luetteloruudusta jonkin tekemättömän tehtävän ja merkitä sen tehdyksi painamalla "Set completed" -nappia. Tehtävän tilan muuttuminen tehdyksi päivitetään SQL-tietokantatauluun. Kyseinen tehtävä siirtyy tehtävänäkymässä toiseen luetteloruutuun, jossa on valmiiksi merkityt tehtävät. Alla olevassa sekvenssikaaviossa on kuvattu sovelluksen toiminta pääpiirteittäin kyseisen käyttötapauksen osalta: 

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant TaskService
  participant TaskRepository
  participant Database@{ "type" : "database" }

  User->>UI: select task: "Finalize your project 10.05.2026"
  User->>UI: click "Set completed" button
  UI->>TaskService: set_completed(selected_task_id)
  TaskService->>TaskRepository: set_completed(task_id)
  TaskRepository->>Database: UPDATE Tasks SET completed = 1 <br/>WHERE id = task_id
  Database-->>TaskRepository:
  TaskRepository-->>TaskService:
  TaskService-->>UI:
  UI->>UI: update_task_view()
  UI->>UI: show_task_view()
```
Kun käyttäjä on valinnut tekemättömän tehtävän ja painaa ”Set completed”-nappia, tapahtumakäsittelijä tarkistaa, että tehtävä on valittu ja kutsuu sovelluslogiikan `TaskService` metodia `set_completed`. Metodi kutsuu luokan `TaskRepository` metodia `set_completed`, joka saa parametriksi valitun tehtävän id:n (`task_id`). Metodi päivittää tietokantaan tehtävän tilan `completed` tehdyksi. Lopuksi kutsutaan käyttöliittymän `UI` metodia `_update_task_view`, joka kutsuu metodia `show_task_view`. Tämän seurauksena käyttöliittymän näkymä `TaskView` päivitetään, jolloin tehdyksi merkitty tehtävä siirtyy tehtyjen tehtävien luetteloon.
