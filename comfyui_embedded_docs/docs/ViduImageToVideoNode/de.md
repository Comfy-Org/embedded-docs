# ViduImageToVideoNode

Der Node Vidu Image To Video Generation erstellt aus einem Startbild und einer optionalen Textbeschreibung ein kurzes Video. Er verwendet ein KI-Modell, um Videoinhalte zu generieren, die vom bereitgestellten Bildframe fortgesetzt werden, und gibt das resultierende Video zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modellname (Standard: viduq1) | COMBO | Ja | `viduq1` |
| `image` | Ein Bild, das als Startframe des generierten Videos verwendet wird | IMAGE | Ja | - |
| `prompt` | Eine Textbeschreibung für die Videogenerierung (Standard: leer) | STRING | Nein | - |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5, festgelegt auf 5 Sekunden) | INT | Nein | 5-5 |
| `seed` | Seed für die Videogenerierung (0 für zufällig) (Standard: 0) | INT | Nein | 0-2147483647 |
| `resolution` | Unterstützte Werte können je nach Modell und Dauer variieren (Standard: 1080p) | COMBO | Nein | `1080p` |
| `movement_amplitude` | Die Bewegungsamplitude von Objekten im Frame (Standard: auto) | COMBO | Nein | `auto`<br>`small`<br>`medium`<br>`large` |

**Einschränkungen:**

- Es ist nur ein Eingabebild zulässig (mehrere Bilder können nicht verarbeitet werden).
- Das Eingabebild muss ein Seitenverhältnis zwischen 1:4 und 4:1 aufweisen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videoausgabe | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `9e3b1ba325c44fcd03207f93030eba1a66507f9613d93135546ab7b6f37f7699`
