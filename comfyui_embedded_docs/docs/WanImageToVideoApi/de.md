# WanImageToVideoApi

Der Wan Image to Video-Node generiert ein Video aus einem einzelnen Eingabebild und einem Text-Prompt. Er verwendet das bereitgestellte Bild als erstes Einzelbild und erstellt eine Videosequenz basierend auf der Beschreibung, mit Optionen für Auflösung, Dauer, Audio und weitere erweiterte Einstellungen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Modell (Standard: "wan2.6-i2v") | COMBO | Ja | "wan2.5-i2v-preview"<br>"wan2.6-i2v" |
| `image` | Eingabebild, das als erstes Einzelbild für die Videogenerierung dient. Es ist genau ein Bild erforderlich. | IMAGE | Ja | - |
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch (Standard: leer). | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt, der beschreibt, was vermieden werden soll (Standard: leer). | STRING | Nein | - |
| `resolution` | Videoauflösungsqualität (Standard: "720P"). Das Wan 2.6-Modell unterstützt kein 480P. | COMBO | Nein | "480P"<br>"720P"<br>"1080P" |
| `duration` | Dauer des generierten Videos in Sekunden. Eine Dauer von 15 Sekunden wird nur vom Wan 2.6-Modell unterstützt (Standard: 5). | INT | Nein | 5-15 (Schrittweite: 5) |
| `audio` | Audio muss eine klare, laute Stimme enthalten, ohne störende Geräusche oder Hintergrundmusik. Wenn Audio bereitgestellt wird, muss die Audiodauer zwischen 3,0 und 29,0 Sekunden liegen. | AUDIO | Nein | - |
| `seed` | Für die Generierung zu verwendender Seed (Standard: 0). | INT | Nein | 0-2147483647 |
| `generate_audio` | Wenn keine Audioeingabe bereitgestellt wird, wird Audio automatisch generiert (Standard: False). | BOOLEAN | Nein | - |
| `prompt_extend` | Ob der Prompt mit KI-Unterstützung erweitert werden soll (Standard: True). | BOOLEAN | Nein | - |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll (Standard: False). | BOOLEAN | Nein | - |
| `shot_type` | Gibt den Aufnahmetyp für das generierte Video an, d. h., ob das Video eine einzelne durchgehende Aufnahme oder mehrere Aufnahmen mit Schnitten ist. Dieser Parameter wird nur wirksam, wenn prompt_extend True ist (Standard: "single"). | COMBO | Nein | "single"<br>"multi" |

**Einschränkungen:**

- Für die Videogenerierung ist genau ein Eingabebild erforderlich.
- Das Wan 2.6-Modell (`wan2.6-i2v`) unterstützt keine 480P-Auflösung.
- Eine Dauer von 15 Sekunden wird nur vom Wan 2.6-Modell (`wan2.6-i2v`) unterstützt.
- Wenn Audio bereitgestellt wird, muss es eine Dauer zwischen 3,0 und 29,0 Sekunden haben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Generiertes Video basierend auf dem Eingabebild und dem Prompt. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/de.md)

---
**Source fingerprint (SHA-256):** `dabcbfa3118669d9ff5b40b79ef643ffcf7ac5e510e61d6ad859d80360061673`
