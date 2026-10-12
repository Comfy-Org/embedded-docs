# SplitSigmasDenoise

Der Knoten SplitSigmasDenoise unterteilt eine Folge von Sigma-Werten anhand eines Parameters für die Denoising-Stärke in zwei Teile. Er teilt die Eingabe-Sigmas in Sequenzen mit hohen und niedrigen Sigma-Werten auf, wobei der Teilungspunkt durch Multiplikation der Gesamtzahl der Schritte (um eins kleiner als die Anzahl der Sigma-Werte) mit dem Denoise-Faktor bestimmt wird. Dadurch kann der Rauschplan in verschiedene Intensitätsbereiche für eine spezialisierte Verarbeitung aufgeteilt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `sigmas` | Die Eingabesequenz von Sigma-Werten, die den Rauschplan darstellt | SIGMAS | Ja | - |
| `denoise` | Der Faktor für die Denoising-Stärke, der bestimmt, an welcher Stelle die Sigma-Sequenz aufgeteilt wird (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `high_sigmas` | Der erste Teil der Sigma-Sequenz, der die höheren Sigma-Werte bis zum Teilungspunkt enthält | SIGMAS |
| `low_sigmas` | Der zweite Teil der Sigma-Sequenz, der die niedrigeren Sigma-Werte ab dem Teilungspunkt enthält | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/de.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
