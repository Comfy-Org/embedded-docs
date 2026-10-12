# KlingFirstLastFrameNode

Dieser Node verwendet das Kling 3.0-Modell, um ein Video zu generieren. Er erstellt das Video basierend auf einem Text-Prompt, einer angegebenen Dauer und zwei bereitgestellten Bildern: einem Startbild und einem Endbild. Der Node kann außerdem begleitendes Audio für das Video generieren.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell- und Generierungseinstellungen. Wenn Sie diese Option auswählen, wird ein verschachtelter Parameter `resolution` angezeigt. | DYNAMIC_COMBO | Ja | `"kling-v3"` |
| `prompt` | Die Textbeschreibung, die die Videogenerierung steuert. Muss zwischen 1 und 2500 Zeichen lang sein. | STRING | Ja | N/A |
| `duration` | Die Länge des Videos in Sekunden (Standard: 5). | INT | Ja | 3 bis 15 |
| `first_frame` | Das Startbild für das Video. Muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 1:2.5 und 2.5:1 aufweisen. | IMAGE | Ja | N/A |
| `end_frame` | Das Endbild für das Video. Muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 1:2.5 und 2.5:1 aufweisen. | IMAGE | Ja | N/A |
| `generate_audio` | Steuert, ob Audio für das Video generiert wird (Standard: True). | BOOLEAN | Ja | N/A |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 bis 2147483647 |

### Kling V3 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Die Auflösung für das generierte Video (Standard: `"1080p"`). | COMBO | Ja | `"4k"`<br>`"1080p"`<br>`"720p"` |

**Hinweis:** Die Bilder `first_frame` und `end_frame` müssen mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 1:2.5 und 2.5:1 aufweisen, damit der Node korrekt funktioniert. Der `prompt` muss zwischen 1 und 2500 Zeichen lang sein. Die Option `resolution` entspricht einem Kling-Generierungsmodus: `"4k"`, `"1080p"` (Pro) und `"720p"` (Standard).

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/de.md)

---
**Source fingerprint (SHA-256):** `b71119c3267e2a74d2180e5182463c78828e892bfcf1eeb7c33a0f4d7019997f`
