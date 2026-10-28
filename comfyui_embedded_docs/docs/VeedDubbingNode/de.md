# VEED Dubbing

VEED Dubbing übersetzt die Sprache in einem Video mit VEED in eine andere Sprache, klont dabei die Stimme jedes Sprechers und synchronisiert die Lippenbewegungen mit der Übersetzung. Der Clip wird hochgeladen, der VEED-Job wird abgefragt, und das synchronisierte Video kommt mit 25 fps zurück; seine Länge entspricht seiner neuen Audiospur. Verwenden Sie es, um einen fertigen Clip zu lokalisieren, ohne neu zu drehen oder die Stimme neu aufzunehmen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Dubbing-Modell. `"standard"` ist günstiger und liefert Mono-Audio, mit lateinamerikanischem Spanisch und brasilianischem Portugiesisch; `"pro"` fügt regionale Akzente und Stereo-Audio hinzu. Bei Auswahl eines Modells werden `video`, `target_language`, `source_language` und `seed` eingeblendet. | DYNAMIC_COMBO | Ja | `"standard"`<br>`"pro"` |

### standard Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"standard"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Video mit sichtbarem Gesicht und Sprache, bis zu 599 Sekunden. Die Ausgabe hat die Länge ihrer Audiospur und wird mit 25 fps wiedergegeben. | VIDEO | Ja | Bis zu 599 Sekunden |
| `target_language` | Sprache, in die synchronisiert werden soll, eine von 85 Sprachen. (Standard: `"English"`) | COMBO | Ja | 85 Sprachen |
| `source_language` | Im Video gesprochene Sprache oder `"auto"`, um sie zu erkennen. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>85 Sprachen |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

### pro Eingaben

Diese Eingaben erscheinen, wenn `model` auf `"pro"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Video mit sichtbarem Gesicht und Sprache, bis zu 599 Sekunden. Die Ausgabe hat die Länge ihrer Audiospur und wird mit 25 fps wiedergegeben. | VIDEO | Ja | Bis zu 599 Sekunden |
| `target_language` | Sprache oder regionaler Akzent, in den synchronisiert werden soll: 87 Sprachen plus 14 Akzente wie `"English (UK)"`, `"Spanish (Mexico)"` und `"Portuguese (Brazil)"`. (Standard: `"English (US)"`) | COMBO | Ja | 101 Optionen |
| `source_language` | Im Video gesprochene Sprache oder `"auto"`, um sie zu erkennen. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>91 Sprachen |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

Der Node bricht mit einem Fehler ab, wenn das Video keine Audiospur hat, wenn der Clip länger als 599 Sekunden ist oder wenn der VEED-Job fehlschlägt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das synchronisierte Video: das Originalmaterial mit der übersetzten Sprache und angepasster Lippenbewegung. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedDubbingNode/de.md)

---
**Source fingerprint (SHA-256):** `fb818ca510e20bccffde61dca98c457984b8a110976e56f2a513f6c7f4d80c80`
