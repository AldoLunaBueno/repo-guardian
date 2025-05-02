# Repo-Guardian

Repo-Guardian es una utilidad CLI y TUI para auditar, reparar y reconstruir la integridad de cualquier repositorio Git, incluso si contiene objetos dañados o historiales reescritos.

Este proyecto implementa escaneo de objetos, validación de DAG, detección de commits reescritos mediante Jaro–Winkler y exportación de grafos en formato GraphML para análisis posterior.

---

## Estado del proyecto

[![Build Status](https://img.shields.io/badge/build-pending-lightgrey)](https://github.com/AldoLunaBueno/repo-guardian/actions)
[![Coverage](https://img.shields.io/badge/coverage-in%20progress-lightgrey)](https://codecov.io/)
[![Release](https://img.shields.io/badge/release-alpha-lightgrey)](https://github.com/AldoLunaBueno/repo-guardian/releases)

---

## Diagrama contextual

![](https://uml.planttext.com/plantuml/svg/NP71JiCm38RlbVeErauWKHw00zhKJMFIX13I90vSlDJR326fOXVsEZmBBuRJbOdr5ENt5__vxQae9kq-V5aegoTufZPMomvJmnZAeYpGQKom4PCuPY6HKmnxOoSP5hOwHrYoJW0bdnVCVkZr6gxcioLyekS6xSdrYJux_NjYBHwwBSoSSWpIS_LgPEm9XM2USAUKUcJGBhZPqmheQ4H0ytya_Ohf_UK6IDt9VyrRoQ66V51Lz-S_mHtKQ_Czt_iYg-aBSHW8uS2IqwCVKRcjOHj1Q34XOFZvzYmiO3CeYterDbgyaUiKX_4uoqqowlcNsU1Z6vF1UPu8j_k4xI5li2oc59f-cRy0)

[Enlace al editor](https://www.planttext.com?text=NP71JiCm38RlbVeErauWKHw00zhKJMFIX13I90vSlDJR326fOXVsEZmBBuRJbOdr5ENt5__vxQae9kq-V5aegoTufZPMomvJmnZAeYpGQKom4PCuPY6HKmnxOoSP5hOwHrYoJW0bdnVCVkZr6gxcioLyekS6xSdrYJux_NjYBHwwBSoSSWpIS_LgPEm9XM2USAUKUcJGBhZPqmheQ4H0ytya_Ohf_UK6IDt9VyrRoQ66V51Lz-S_mHtKQ_Czt_iYg-aBSHW8uS2IqwCVKRcjOHj1Q34XOFZvzYmiO3CeYterDbgyaUiKX_4uoqqowlcNsU1Z6vF1UPu8j_k4xI5li2oc59f-cRy0)

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
