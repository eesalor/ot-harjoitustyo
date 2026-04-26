# Sovelluksen arkkitehtuuri

## Pakkauskaavio arkkitehtuurista
 ![Pakkauskaavio arkkitehtuurista](/dokumentaatio/kuvat/pakkauskaavio_arkkitehtuuri.png)


## Luokkakaaviot

Kuvaus `Task`-luokasta, jossa määritellään sovellukseen lisättävän tehtävän rakenne.
Kuvaus `Category`-luokasta, jossa määritellään sovellukseen lisättävän aihekategorian rakenne.

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

## Pakkauskaavio arkkitehtuurista luokilla
![Pakkauskaavio arkkitehtuurista](/dokumentaatio/kuvat/pakkauskaavio_arkkitehtuuri_luokilla.png)



## Sovelluksen päätoiminnallisuudet

### Tehtävän lisääminen
Käyttäjä voi lisätä uuden tehtävän ollessaan sovelluksen päänäkymässä eli tehtävänäkymässä. Käyttäjä voi syöttää tekstikenttiin tehtävän kuvauksen ja määräajan ja lisätä uuden tehtävän painamalla "Create"-nappia. Oletuksena tehtävän tila on tekemätön. Tehtävän otsikko, määräaika ja tila tallennetaan SQL-tietokantatauluun. Lisätty tehtävä ilmestyy lopulta tehtävänäkymässä olevaan luetteloruutuun. Alla olevassa sekvenssikaaviossa on kuvattu sovelluksen toiminta pääpiirteittäin kyseisen käyttötapauksen osalta:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant TaskService
  participant TaskRepository
  participant task
  participant Database@{ "type" : "database" }

  User->>UI: enter title: "Finalize your project"
  User->>UI: enter date: "10.05.2026"
  User->>UI: click "Create" button
  UI->>TaskService: create_task("Finalize your project", "10.05.2026")
  TaskService->>task: Task("Finalize your project", "10.05.2026")
  TaskService->>TaskRepository: create_task(task)
  TaskRepository->>Database: INSERT INTO Tasks (title, date, completed) <br/>VALUES (task.title, task.date, 0);
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
