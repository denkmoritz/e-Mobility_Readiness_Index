# SII Final Project


am besten einfach alle neuen Packages in die **requirements.txt** packen.
Base Python Interpreter 3.11

## Setup Instructions

### 1. Clone the repository


```bash
git clone https://github.com/denkmoritz/e-Mobility_Readiness_Index.git
```
```bash
cd e-Mobility_Reainess_Index
```

### 2 start docker

das aktuelle docker compose enthält die Datenbank mit den entsprechenden Daten.
Wenn ihr die via PGAdmin einsehen wollt müsst ihr die verbinden. die config daten stehen in den Dateien.
wichtig ist dass die verbindung über localhost läuft (erstes feld).

```bash
docker compose up -d
```