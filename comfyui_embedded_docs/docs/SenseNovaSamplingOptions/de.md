# SenseNova-Sampling-Optionen

SenseNova Sampling Options legt den SenseNova-Flow-Shift für ein Modell fest. Es klont das Eingabemodell, fügt mit dem gewählten Flow-Shift-Wert eine Sampling-Konfiguration für das SenseNova-Modell hinzu und gibt das gepatchte Modell zur Verwendung während des Samplings zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, auf das die SenseNova-Flow-Shift-Sampling-Konfiguration angewendet wird. | MODEL | Ja | - |
| `shift` | Der Flow-Shift-Wert, der für das Sampling des SenseNova-Modells festgelegt wird (Standard: 3.0; UI-Schrittweite: 0.01). | FLOAT | Ja | Kein Minimum oder Maximum definiert |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `MODEL` | Eine Kopie des Eingabemodells, bei der der SenseNova-Flow-Shift auf die Sampling-Konfiguration angewendet wurde. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaSamplingOptions/de.md)

---
**Source fingerprint (SHA-256):** `b0dea4a5c226bccb54bb1d70e8ea2791a645018853571429c556034351e9e75a`
