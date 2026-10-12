# Vidu3ImageToVideoNode

Der Node „Vidu Q3 Image-to-Video Generation“ erstellt eine Videosequenz ausgehend von einem Eingabebild. Er verwendet ein Vidu Q3-Modell, um das Bild zu animieren, optional geleitet durch einen Text-Prompt, und gibt eine Videodatei aus.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell zur Videogenerierung. | DYNAMIC_COMBO | Ja | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `image` | Ein Bild, das als Startframe des generierten Videos verwendet wird. | IMAGE | Ja | - |
| `prompt` | Ein optionaler Text-Prompt für die Videogenerierung (max. 2000 Zeichen) (Standard: leer). | STRING | Ja | - |
| `seed` | Der Seed-Wert, der verwendet wird, um die Zufälligkeit der Generierung zu steuern (Standard: 1). | INT | Ja | 0 bis 2147483647 |

### viduq3-pro Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | `"720p"`<br>`"1080p"`<br>`"2K"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 1 bis 16 |
| `audio` | Wenn aktiviert, wird das Video mit Ton ausgegeben (einschließlich Dialogen und Soundeffekten) (Standard: False). | BOOLEAN | Ja | `True`<br>`False` |

### viduq3-turbo Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 1 bis 16 |
| `audio` | Wenn aktiviert, wird das Video mit Ton ausgegeben (einschließlich Dialogen und Soundeffekten) (Standard: False). | BOOLEAN | Ja | `True`<br>`False` |

**Hinweis:** Der Parameter `image` muss ein Seitenverhältnis zwischen 1:4 und 4:1 aufweisen (Hochformat bis Querformat). Der Parameter `prompt` ist optional, darf jedoch 2000 Zeichen nicht überschreiten. Die verfügbaren Optionen für `resolution` hängen vom ausgewählten Modell ab: `"viduq3-pro"` unterstützt `"720p"`, `"1080p"` und `"2K"`; `"viduq3-turbo"` unterstützt `"720p"` und `"1080p"`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `77500d1e19928128decc010540670e311cd8ec4fcad913412517f47f0e27e15f`
