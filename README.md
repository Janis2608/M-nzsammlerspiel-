# Münzsammlerspiel (Coin Collector)

Ein 2D-Top-Down-Spiel, entwickelt mit **Python**, **Pygame**, **Pydantic** und **Typer**.  
Ziel: Sammle alle Münzen in einem Level ein, ohne durch Hindernisse (Wände) laufen zu können.

---

## Funktionen

- **Level aus JSON**: Level werden aus JSON-Dateien geladen (z. B. `level_example.json`).
- **Datenvalidierung**: Strikte Validierung der Level-Dateien durch **Pydantic**.
- **CLI-Start**: Start über die Kommandozeile mit **Typer** (`--level`, `--fps`, `--debug`).
- **Kollisionserkennung**: Rechteck-Rechteck-Kollision zwischen Spieler und Wänden.
- **Münzen sammeln**: Münzen können eingesammelt werden.
- **Debug-Modus**: Optionale Anzeige von Debug-Informationen (`--debug`).

---

## Voraussetzungen

Bitte stelle sicher, dass Folgendes installiert ist:

- **Python 3.11 oder neuer**
- **uv** (schneller Python-Paket- und Projektmanager)

---

## Installation

### 1) Projekt öffnen
Öffne das Projekt im Explorer oder in VS Code und gehe im Terminal in das Hauptverzeichnis des Projekts:

```powershell
cd "C:\Schule\Software Entwicklung\coin_collector"

## Starten des Spiels
uv run -m coin_collector --level coin_collector/levels/level_example.json --fps 60 --debug
