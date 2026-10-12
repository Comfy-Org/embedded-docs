# Vidu Q3 Text-zu-Video-Generierung

Der Node Vidu Q3 Text-to-Video Generation erstellt ein Video aus einer Textbeschreibung. Er verwendet das Modell Vidu Q3 Pro oder Q3 Turbo, um Videoinhalte basierend auf Ihrem Prompt zu generieren, sodass Sie die Länge, Auflösung, das Seitenverhältnis und ob Audio enthalten ist, steuern können.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Modell, das für die Videogenerierung verwendet werden soll. Die Auswahl eines Modells blendet zusätzliche Konfigurationsparameter für Seitenverhältnis, Auflösung, Dauer und Audio ein. | DYNAMIC_COMBO | Ja | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `prompt` | Eine textuelle Beschreibung für die Videogenerierung mit einer maximalen Länge von 2000 Zeichen. | STRING | Ja | N/A |
| `seed` | Ein Seed-Wert zur Steuerung der Zufälligkeit der Generierung (Standard: 1). | INT | Ja | 0 bis 2147483647 |

### viduq3-pro und viduq3-turbo Eingaben

Die folgenden Konfigurationsparameter werden von den Modellen `viduq3-pro` und `viduq3-turbo` gemeinsam verwendet.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5). | INT | Ja | 1 bis 16 |
| `audio` | Wenn aktiviert, wird Video mit Ton ausgegeben (einschließlich Dialogen und Soundeffekten) (Standard: False). | BOOLEAN | Ja | True/False |

**Hinweis:** Die Parameter `aspect_ratio`, `resolution`, `duration` und `audio` sind erforderlich, sobald ein `model` ausgewählt wurde, da sie Teil seiner Konfiguration sind. Der `prompt` darf nicht leer sein und darf 2000 Zeichen nicht überschreiten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `89c23454375a43cdfaf46c9e0e55a8a8166d02ada47ca2e237bd9f73fa4d78db`
