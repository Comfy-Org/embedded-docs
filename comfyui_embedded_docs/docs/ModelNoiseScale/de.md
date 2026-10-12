# ModelNoiseScale

Dieser Node passt die Rauschskala an, die während des Modell-Samplings verwendet wird. Er erstellt eine Kopie des Eingabemodells, wendet die angegebene Rauschskala auf dessen Sampling-Konfiguration an und gibt das modifizierte Modell zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das die Anpassung der Rauschskala angewendet wird. | MODEL | Ja | - |
| `noise_scale` | Absolute Trainings-Rauschskala. Zum Beispiel HiDream-O1 base: 8.0, dev: 7.5. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 64.0 (Schritt: 0.01) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Das modifizierte Modell mit der neu angewendeten Rauschskala. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/de.md)

---
**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`
