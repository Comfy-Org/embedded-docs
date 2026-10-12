# Vidu2StartEndToVideoNode

Dieser Node erzeugt ein Video, indem er zwischen einem bereitgestellten Startbild und einem Endbild interpoliert, gesteuert durch einen Text-Prompt. Er verwendet ein angegebenes Vidu-Modell, um über eine festgelegte Dauer einen fließenden Übergang zwischen den beiden Bildern zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Vidu-Modell, das für die Videogenerierung verwendet wird. | COMBO | Ja | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` |
| `first_frame` | Das Startbild für die Videosequenz. Es ist nur ein einzelnes Bild zulässig. | IMAGE | Ja | - |
| `end_frame` | Das Endbild für die Videosequenz. Es ist nur ein einzelnes Bild zulässig. | IMAGE | Ja | - |
| `prompt` | Prompt-Beschreibung (max. 2000 Zeichen). | STRING | Ja | - |
| `duration` | Die Länge des generierten Videos in Sekunden (Standard: 5). | INT | Nein | 2 bis 8 |
| `seed` | Eine Zahl zur Initialisierung der Zufallsgenerierung für reproduzierbare Ergebnisse (Standard: 1). | INT | Nein | 0 bis 2147483647 |
| `resolution` | Die Ausgabeauflösung des generierten Videos. | COMBO | Nein | `"720p"`<br>`"1080p"` |
| `movement_amplitude` | Die Bewegungsamplitude von Objekten im Frame. | COMBO | Nein | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Hinweis:** Die Bilder `first_frame` und `end_frame` müssen ähnliche Seitenverhältnisse haben. Der Node validiert, dass ihre Seitenverhältnisse innerhalb eines relativen Bereichs von 0,8 bis 1,25 liegen. Für jede Eingabe ist nur ein Bild zulässig.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `01316d15f95f264cadfb33978565fc320a9f42917693faa87c1367c0f31ca400`
