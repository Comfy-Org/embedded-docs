# PixverseTextToVideoNode

Generiert Videos aus einem Text-Prompt mithilfe der PixVerse API. Der Node ermöglicht es, Form, Qualität, Länge und Bewegungsstil des Videos zu steuern und optional eine gespeicherte Stilvorlage anzuwenden. Er übermittelt die Anfrage, wartet auf den Abschluss der Generierung und gibt das fertige Video zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Videogenerierung (Standard: "") | STRING | Ja | Muss mindestens 1 Zeichen enthalten |
| `aspect_ratio` | Seitenverhältnis für das generierte Video | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `quality` | Einstellung für die Videoqualität (Standard: "540p") | COMBO | Ja | `"540p"`<br>`"1080p"` |
| `duration_seconds` | Dauer des generierten Videos in Sekunden | COMBO | Ja | `"5"`<br>`"10"` |
| `motion_mode` | Bewegungsstil für die Videogenerierung | COMBO | Ja | `"normal"`<br>`"fast"` |
| `seed` | Seed für die Videogenerierung (Standard: 0) | INT | Ja | 0 bis 2147483647 |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente in einem Bild (Standard: "") | STRING | Nein | - |
| `pixverse_template` | Eine optionale Vorlage zur Beeinflussung des Generierungsstils, erstellt vom PixVerse Template-Node | CUSTOM | Nein | - |

**Hinweis:** Der `prompt` muss mindestens 1 Zeichen enthalten. Wenn die Qualität 1080p ausgewählt wird, wird der Bewegungsmodus automatisch auf `normal` gesetzt und die Dauer auf 5 Sekunden begrenzt. Bei jeder anderen Dauer als 5 Sekunden wird der Bewegungsmodus ebenfalls automatisch auf `normal` gesetzt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`
