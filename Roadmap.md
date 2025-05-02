# Roadmap

| Épica | Historia | Tarea | Prioridad | Etiqueta Kanban |
|:---:|:---:|:---:|:---:|:---:|
| E-01 | RX-01 | Crear repositorio | 3 | Done |
| E-01 | RX-02 | Plantillas | 5 | Done |
| E-01 | RX-03 | Configurar CI  | 5 | Done |
| E-01 | RX-04 | Roadmap | 3 | Done |

| Épica | Historia | Tarea | Prioridad | Etiqueta Kanban |
| :---: | :---: | :---: | :---: | :---: |
|  E-02 |   RX-5  |         Implementar `read_loose(path)`        |     5     |      Backlog      |
|  E-02 |   RX-6  | Agregar 6 pruebas unitarias para `read_loose` |     5     |      Backlog      |
|  E-02 |   RX-7  |       Añadir `fixtures/corrupt-blob.git`      |     3     |      Backlog      |
|  E-02 |   RX-8  |        Parsear packfile header e índice       |     5     |      Backlog      |
|  E-02 |   RX-9  |    Implementar escenario BDD "blob dañado"    |     4     |      Backlog      |
|  E-02 |   RX-10  |            Asegurar cobertura ≥ 60%           |     4     |      Backlog     |

| Épica | Historia |                        Tarea                         | Prioridad | Etiqueta Kanban |
| :---: | :------: | :--------------------------------------------------: | :-------: | :-------------: |
|  E-03 |   RX-11  |           Redactar `docs/dag.mmd` (Mermaid)          |     3     |      -      |
|  E-03 |   RX-12  |     Implementar `build_graph(objects)` → DiGraph     |     5     |      -      |
|  E-03 |   RX-13  |      Implementar `jw_detector.is_rewrite(a, b)`      |     5     |      -      |
|  E-03 |   RX-14  | Crear hook `post-merge` que exporta y sube a Release |     4     |      -      |
|  E-03 |   RX-15  |         Generar release draft `v0.5.0-alpha`         |     3     |      -      |

| Épica | Historia |                          Tarea                           | Prioridad | Etiqueta Kanban |
| :---: | :------: | :------------------------------------------------------: | :-------: | :-------------: |
|  E-04 |   RX-16  | Diseñar wireframe de TUI y grabar demo (GIF o asciinema) |     3     |      -     |
|  E-04 |   RX-17  |           Implementar `cli.py` con subcomandos           |     5     |      -     |
|  E-04 |   RX-18  |             Implementar script `scan-repo.sh`            |     4     |      -     |
|  E-04 |   RX-19  |         Agregar autocompletado con `argcomplete`         |     3     |      -     |
|  E-04 |   RX-20  |         CI con `pytest -n auto` + reportes JUnit         |     4     |      -     |

| Épica | Historia |                      Tarea                      | Prioridad | Etiqueta Kanban |
| :---: | :------: | :---------------------------------------------: | :-------: | :-------------: |
|  E-05 |   RX-21  |    Implementar `bench.py` con tabla Markdown    |     4     |      -      |
|  E-05 |   RX-22  |  Agregar gráficos PNG a MkDocs con `matplotlib` |     3     |      -      |
|  E-05 |   RX-23  |       Publicar site con `mkdocs gh-deploy`      |     4     |      -      |
|  E-05 |   RX-24  | Grabar y editar video de presentación (≤ 5 min) |     3     |      -      |
|  E-05 |   RX-25  |   Empaquetar con `pip`, publicar release final  |     5     |      -      |
