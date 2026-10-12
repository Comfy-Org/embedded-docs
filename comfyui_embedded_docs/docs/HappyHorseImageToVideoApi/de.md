# HappyHorse Bild zu Video

Dieser Node erzeugt mit dem HappyHorse-Modell ein kurzes Video aus einem einzelnen Startbild. Sie geben ein Bild für das erste Frame und einen Text-Prompt an, der die gewünschte Bewegung und Szene beschreibt, und der Node erstellt ein Video, das von diesem Bild fortgesetzt wird.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das HappyHorse-Modell, das für die Videogenerierung verwendet wird. | DYNAMIC_COMBO | Ja | `"happyhorse-1.1-i2v"`<br>`"happyhorse-1.0-i2v"` |
| `first_frame` | Bild des ersten Frames. Das Seitenverhältnis der Ausgabe wird aus diesem Bild abgeleitet. | IMAGE | Ja | 300×300 px min; 1:2.5 bis 2.5:1 |
| `seed` | Seed für die Generierung. (Standard: 0) | INT | Ja | 0 bis 2147483647 |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll. (erweiterte Option; Standard: False) | BOOLEAN | Ja | True / False |

### happyhorse-1.1-i2v- und happyhorse-1.0-i2v-Eingaben

Beide Modellversionen verwenden denselben Parametersatz.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch. (Standard: "") | STRING | Nein | N/A |
| `resolution` | Die Auflösung des Ausgabevideos. (Standard: `"720P"`) | COMBO | Ja | `"720P"`<br>`"1080P"` |
| `duration` | Die Dauer des generierten Videos in Sekunden. (Standard: 5) | INT | Ja | 3 bis 15 |

Hinweis: Das Bild `first_frame` muss mindestens 300x300 Pixel groß sein, und sein Seitenverhältnis muss zwischen 1:2.5 und 2.5:1 liegen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/de.md)

---
**Source fingerprint (SHA-256):** `4bf6eece0d1b4104ce2d84e29b2c918a0a6ba782da1dd801b66cbfa1666d150b`
