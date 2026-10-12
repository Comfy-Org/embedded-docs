# Bria Video Greenscreen

Dieser Node ersetzt den Hintergrund eines Videos durch einen einfarbigen Chroma-Key-Hintergrund mithilfe der Bria API. Er verarbeitet das eingegebene Video und gibt ein neues Video zurück, bei dem der ursprüngliche Hintergrund entfernt und durch eine einheitliche grüne oder blaue Bildschirmfarbe ersetzt wurde.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Das zu verarbeitende Eingabevideo | VIDEO | Ja | Videodatei |
| `green_shade` | Einfarbiger Chroma-Key-Farbton, der hinter dem Vordergrund angewendet wird: `broadcast_green` (#00B140), `chroma_green` (#00FF00) oder `blue_screen` (#0000FF). | COMBO | Ja | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 bis 2147483647 |

**Hinweis:** Das Eingabevideo darf eine Dauer von 60 Sekunden nicht überschreiten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das verarbeitete Video (MP4, H.264), bei dem der ursprüngliche Hintergrund durch den ausgewählten Chroma-Key-Farbton ersetzt wurde | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/de.md)

---
**Source fingerprint (SHA-256):** `70d2951d0adbbe7492b2bc97d04be6591b65f040ca4b414754ad6365c5db45cf`
