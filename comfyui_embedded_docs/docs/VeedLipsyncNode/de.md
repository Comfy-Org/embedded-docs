# VEED Lipsync 2.0

Synchronisieren Sie den Mund eines Sprechers in einem Video mit VEED Lipsync neu auf eine neue Sprachspur. Verwenden Sie dies, um einen Clip zu vertonen oder seinen Dialog zu ersetzen, während das Originalmaterial erhalten bleibt. Die Ausgabe behält die Videoauflösung bei und läuft mit 25 fps; sie ist so lang wie das Audio, mit einem Sprecher pro Video.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Modell. Beim Auswählen eines Modells werden die für dieses Modell spezifischen Parameter angezeigt: `video`, `audio` und `seed`. | DYNAMIC_COMBO | Ja | `"lipsync-2.0"` |
| `video` | Filmmaterial eines Sprechers in Frontalansicht. Wenn es kürzer als das Audio ist, wird es vorwärts und rückwärts abgespielt, bis das Audio endet. | VIDEO | Ja | - |
| `audio` | Neue Sprachaufnahme, bis zu 600 Sekunden. Legt die Videolänge fest. | AUDIO | Ja | Bis zu 600 Sekunden |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 2147483647 |

Der Node bricht mit einem Fehler ab, wenn die Sprachspur länger als 600 Sekunden ist oder wenn der VEED-Job fehlschlägt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `VIDEO` | Das neu synchronisierte Video: das Originalmaterial mit dem an die neue Sprache angepassten Mund. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedLipsyncNode/de.md)

---
**Source fingerprint (SHA-256):** `1a1e854b6923b5bad0fd6f3a79e76c70231dee31a12e9cf0b22be6bdcc741168`
