# PixverseTransitionVideoNode

Erzeugt ein Übergangsvideo zwischen zwei Eingabebildern mithilfe der PixVerse API. Sie geben ein Startbild und ein Endbild an, und der Node erstellt ein flüssiges Video, das vom einen zum anderen übergeht, gesteuert durch Ihren Text-Prompt und die ausgewählten Einstellungen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `first_frame` | Das Startbild für den Videoübergang | IMAGE | Ja | - |
| `last_frame` | Das Endbild für den Videoübergang | IMAGE | Ja | - |
| `prompt` | Prompt für die Videogenerierung (Standard: leerer String) | STRING | Ja | - |
| `quality` | Einstellung für die Videoqualität (Standard: `"540p"`) | COMBO | Ja | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration_seconds` | Videodauer in Sekunden | COMBO | Ja | `5`<br>`8` |
| `motion_mode` | Bewegungsstil für den Übergang (Standard: `"normal"`) | COMBO | Ja | `"normal"`<br>`"fast"` |
| `seed` | Seed für die Videogenerierung (Standard: 0) | INT | Ja | 0 to 2147483647 |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente auf einem Bild (Standard: leerer String) | STRING | Nein | - |

**Hinweis zu Parameterbeschränkungen:** Bei Verwendung der 1080p-Qualität wird der Bewegungsmodus automatisch auf `"normal"` gesetzt und die Dauer ist auf 5 Sekunden begrenzt. Bei jeder Dauer, die nicht 5 Sekunden beträgt, wird der Bewegungsmodus ebenfalls automatisch auf `"normal"` gesetzt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das generierte Übergangsvideo | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `9774f15ae93377d4768cee9f51ce004a791ecaad3cadd0a2467d354c4dbc6f23`
