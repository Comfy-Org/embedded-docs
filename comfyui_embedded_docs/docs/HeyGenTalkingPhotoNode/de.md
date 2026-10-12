# HeyGenTalkingPhotoNode

Animieren Sie ein Standbild einer Person mit der Avatar-IV-Technologie von HeyGen zu einem sprechenden Video mit Lippensynchronisation. Sie können die Animation mit einem Textskript steuern, das HeyGen in Sprache umwandelt, oder eigenes Audio bereitstellen, zu dem der Avatar lippensynchronisiert wird.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Bild einer Person, die animiert werden soll. Wird automatisch herunterskaliert, wenn es größer als 2K ist. | IMAGE | Ja | - |
| `speech` | Steuern Sie den Avatar mit einem Textskript (HeyGen-Text-to-Speech) oder mit eigenem Audio. | DYNAMIC_COMBO | Ja | `"script"`<br>`"audio"` |
| `resolution` | Auflösung des Ausgabevideos (Standard: `"1080p"`). | COMBO | Nein | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Seitenverhältnis der Ausgabe. `"auto"` folgt dem Eingabebild (Standard: `"auto"`). | COMBO | Nein | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `expressiveness` | Wie ausdrucksstark das animierte Gesicht und die Gesten sind (Standard: `"low"`). | COMBO | Nein | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Wird nicht an HeyGen gesendet; ändern Sie ihn, um eine erneute Ausführung zu erzwingen (Standard: 42). | INT | Nein | 0 bis 2147483647 |

### Skript-Eingaben

Wird angezeigt, wenn `speech` `"script"` ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `text` | Text, den der Avatar sprechen soll (bis zu 5000 Zeichen). Die generierte Sprache muss mindestens 1 Sekunde lang sein. (Standard: leer) | STRING | Ja | 1 bis 5000 Zeichen |
| `voice` | Stimme für das Skript (die beliebtesten Stimmen von HeyGen). | COMBO | Ja | Mehrere Optionen verfügbar |
| `custom_voice_id` | Optionale HeyGen-Stimmen-ID. Wenn festgelegt, überschreibt sie die oben ausgewählte Stimme. Jede Stimme aus der HeyGen-Bibliothek (2000+) kann verwendet werden. (Standard: leer) | STRING | Nein | - |
| `voice_speed` | Multiplikator für die Sprechgeschwindigkeit (Standard: 1.0). | FLOAT | Nein | 0.5 bis 1.5 (Schritt 0.05) |

### Audio-Eingaben

Wird angezeigt, wenn `speech` `"audio"` ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `audio` | Audio, zu dem der Avatar lippensynchronisiert wird, bis zu 10 Minuten. | AUDIO | Ja | Bis zu 10 Minuten |

Hinweis: Wenn `speech` `"script"` ist, muss `text` angegeben werden, und eine Stimme ist erforderlich – entweder über den `voice`-Selektor (wobei etwas anderes als die Standardstimme des Avatars ausgewählt wird) oder über eine `custom_voice_id`. Wenn `speech` `"audio"` ist, ist stattdessen `audio` erforderlich.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Generiertes Video des animierten sprechenden Fotos mit lippensynchronisierter Sprache. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTalkingPhotoNode/de.md)

---
**Source fingerprint (SHA-256):** `2181066a8c6191cfcaa15ece4f89a16c37e76aa22763d6df4007baa20336f05a`
