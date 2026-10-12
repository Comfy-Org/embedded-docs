# VAE-Gerät auswählen

## Übersicht

Dieser Node ermöglicht es Ihnen, manuell auszuwählen, auf welchem GPU-Gerät das VAE-Modell platziert werden soll. Standardmäßig wird der VAE auf dem vom Modell-Loader zugewiesenen Gerät platziert, aber Sie können ihn an eine bestimmte GPU binden (z. B. `gpu:0`, `gpu:1`). Wenn das ausgewählte Gerät auf Ihrem Rechner nicht verfügbar ist, reicht der Node den VAE unverändert durch und protokolliert eine Meldung, anstatt fehlzuschlagen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `vae` | Das VAE-Modell, das einem bestimmten Gerät zugewiesen werden soll. | VAE | Ja |  |
| `device` | Das Zielgerät für den VAE. `"default"` stellt das vom Loader zugewiesene Gerät wieder her. `"gpu:N"` bindet den VAE an die N-te verfügbare GPU. CPU ist keine unterstützte Auswahl und wird ignoriert, falls angegeben. (Standard: `"default"`) | COMBO | Ja | `"default"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `vae` | Das VAE-Modell, jetzt dem ausgewählten Gerät zugewiesen. Wenn das angeforderte Gerät nicht verfügbar oder ungültig ist, wird der VAE unverändert durchgereicht. | VAE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectVAEDevice/de.md)

---
**Source fingerprint (SHA-256):** `011154043fc02f930b0074de656bb24baf4dfe74bcfd2e89ea76284f0a5b7d8e`
