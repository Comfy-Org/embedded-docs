# Grok Video erweitern

Der Node Grok Video Extend erweitert ein vorhandenes Video um eine nahtlose Fortsetzung basierend auf einem Text-Prompt. Geben Sie ein kurzes Quellvideo an und beschreiben Sie, was als Nächstes passieren soll; der Node gibt einen neuen Videoclip zurück, der das Original fortsetzt.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Videoerweiterung zu verwendende Modell. Wenn die Option `"grok-imagine-video"` ausgewählt wird, werden ihre modellspezifischen Einstellungen angezeigt. | DYNAMIC_COMBO | Ja | `"grok-imagine-video"` |
| `prompt` | Textbeschreibung dessen, was als Nächstes im Video passieren soll. | STRING | Ja | N/A |
| `video` | Quellvideo, das erweitert werden soll. MP4-Format, 2–15 Sekunden. | VIDEO | Ja | MP4, 2–15 Sekunden, maximal 50 MB |
| `seed` | Der Parameter `seed` bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 bis 2147483647 |

### grok-imagine-video Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `duration` | Länge der Erweiterung in Sekunden (Standard: 8). | INT | Ja | 2 bis 10 |

**Parametereinschränkungen:**
*   Die Eingabe `video` muss eine MP4-Datei mit einer Länge zwischen 2 und 15 Sekunden sein und darf eine Dateigröße von 50 MB nicht überschreiten.
*   Der `prompt` muss nach dem Entfernen von Leerzeichen mindestens ein Zeichen enthalten.
*   Der Parameter `model` ist ein dynamisches Kombinationsfeld. Wenn die Option `"grok-imagine-video"` ausgewählt wird, wird der verschachtelte Parameter `duration` angezeigt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die neu generierte Videoerweiterung. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/de.md)

---
**Source fingerprint (SHA-256):** `5009c007b6f93cd44f2742b024b65f1ac92ab9bca3b85a55554b1d99649e323b`
