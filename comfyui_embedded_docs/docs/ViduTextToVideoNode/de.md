# Vidu Text-zu-Video-Generierung

Der Node „Vidu Text To Video Generation“ erstellt Videos aus Textbeschreibungen. Er verwendet das Vidu-Videogenerierungsmodell, um Ihre Text-Prompts in Videoinhalte mit anpassbaren Einstellungen für Dauer, Seitenverhältnis und visuellen Stil umzuwandeln.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Modellname | COMBO | Ja | `viduq1` |
| `prompt` | Eine textuelle Beschreibung für die Videogenerierung | STRING | Ja | - |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5) | INT | Nein | 5-5 |
| `seed` | Seed für die Videogenerierung (0 für zufällig) (Standard: 0) | INT | Nein | 0-2147483647 |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos | COMBO | Nein | `16:9`<br>`9:16`<br>`1:1` |
| `resolution` | Unterstützte Werte können je nach Modell und Dauer variieren | COMBO | Nein | `1080p` |
| `movement_amplitude` | Die Bewegungsamplitude von Objekten im Frame | COMBO | Nein | `auto`<br>`small`<br>`medium`<br>`large` |

**Hinweis:** Das Feld `prompt` ist erforderlich und darf nicht leer sein. Der Parameter `duration` ist derzeit auf 5 Sekunden festgelegt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Das generierte Video basierend auf dem Text-Prompt | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `913efbb516c40e03ced1fef59905c7efa7737f0506368c9afcacb3b65aa4af66`
