# Repo-Guardian

Repo-Guardian es una utilidad CLI y TUI para auditar, reparar y reconstruir la integridad de cualquier repositorio Git, incluso si contiene objetos dañados o historiales reescritos.

Este proyecto implementa escaneo de objetos, validación de DAG, detección de commits reescritos mediante Jaro–Winkler y exportación de grafos en formato GraphML para análisis posterior.

---

## Estado del proyecto

[![Build Status](https://img.shields.io/badge/build-pending-lightgrey)](https://github.com/AldoLunaBueno/repo-guardian/actions)
[![Coverage](https://img.shields.io/badge/coverage-in%20progress-lightgrey)](https://codecov.io/)
[![Release](https://img.shields.io/badge/release-alpha-lightgrey)](https://github.com/AldoLunaBueno/repo-guardian/releases)

---

## Comandos principales

| Comando                         | Descripción                                       |
|--------------------------------|---------------------------------------------------|
| `guardian scan /ruta`          | Escanea y verifica los objetos de un repo Git    |
| `guardian export-graph`        | Exporta el grafo de commits a formato GraphML     |
| `guardian stats`               | Muestra estadísticas básicas del repositorio     |
| `./scan-repo.sh --repair`      | Ejecuta escaneo con reparación automática        |

---

## Instalación rápida

```bash
pip install repo-guardian
```
