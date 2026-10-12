# SAM3-Tracking-Vorschau

## Übersicht

Dieser Node erstellt eine Videovorschau verfolgter Objekte, wobei jedes verfolgte Objekt mit einer eigenen Farbüberlagerung und einer Nummernbeschriftung gezeichnet wird. Er gibt keine Bild- oder Video-Tensoren aus – stattdessen speichert er das resultierende Vorschauvideo direkt in einer temporären Datei.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `track_data` | Die Tracking-Daten, die gepackte Masken und Objektinformationen von einem SAM3-Tracking-Node enthalten. | TRACK_DATA | Ja | - |
| `images` | Optionale Eingabebilder, die als Hintergrund für die Vorschau verwendet werden. Wenn nicht angegeben, wird ein schwarzer Hintergrund verwendet. | IMAGE | Nein | - |
| `opacity` | Die Deckkraft der Farbüberlagerung, die auf verfolgte Objekte angewendet wird (Standard: 0.5). | FLOAT | Nein | 0.0 bis 1.0 (Schritt: 0.05) |
| `fps` | Die Bildrate des Ausgabevideos (Standard: 24.0). | FLOAT | Nein | 1.0 bis 120.0 (Schritt: 1.0) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `ui` | Ein UI-Element, das das generierte Vorschauvideo anzeigt. Es werden keine Tensordaten zurückgegeben. | PREVIEW_VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackPreview/de.md)

---
**Source fingerprint (SHA-256):** `76389f354c8acdf249137d966765069d530034a0f8eeb39d769bde3c0f7a1bd0`
