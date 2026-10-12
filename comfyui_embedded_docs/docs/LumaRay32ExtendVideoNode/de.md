# LumaRay32ExtendVideoNode

Luma Ray 3.2 Extend Video setzt eine vorherige Luma Ray 3.2-Videogenerierung fort, indem ein neues 5-Sekunden-Segment entweder nach dem ursprünglichen Clip (Vorwärts) oder davor (Rückwärts) erstellt wird. Verbinden Sie die `generation_id`-Ausgabe eines früheren Luma Ray 3.2-Nodes, um diesen Clip als Startframe (Vorwärts) oder Endframe (Rückwärts) der Erweiterung zu verwenden. Erweiterungen sind immer 5 Sekunden lang.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `source_generation_id` | Generierungs-ID des vorherigen Ray 3.2-Videos, das erweitert werden soll. Verbinden Sie die `generation_id`-Ausgabe eines anderen Luma Ray 3.2-Nodes. Standard: "" (leer). Dieser Wert ist erforderlich und darf nicht leer sein. | STRING | Ja | – |
| `direction` | Vorwärts setzt nach dem vorherigen Clip fort; rückwärts wird davor eingefügt. Vorwärts verwendet den Quellclip als Startframe; rückwärts verwendet ihn als Endframe. Die Auswahl von "Forward (continue after)" fügt die Option `loop` hinzu. | DYNAMIC_COMBO | Ja | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `prompt` | Text-Prompt für den neuen Inhalt. Standard: "" (leer). Muss zwischen 1 und 6000 Zeichen lang sein. | STRING | Ja | 1 bis 6000 Zeichen |
| `resolution` | Ausgabeauflösung für das erweiterte Videosegment. Standard: "720p". | COMBO | Ja | "540p"<br>"720p"<br>"1080p" |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 0. | INT | Ja | 0 bis 0xFFFFFFFFFFFFFFFF (18446744073709551615) |

### Forward (continue after) Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `loop` | Das erweiterte Video nahtlos in Schleife wiedergeben (nur Vorwärtserweiterung). Standard: False. | BOOLEAN | Nein | True<br>False |

### Backward (lead-in before) Eingaben

Diese Richtung fügt keine zusätzlichen Parameter hinzu.

**Hinweis:** Erweiterungen sind immer 5 Sekunden lang. Der Parameter `loop` ist nur verfügbar, wenn `direction` auf "Forward (continue after)" gesetzt ist; bei Verwendung von "Backward (lead-in before)" ist die Option `loop` nicht verfügbar. Der `prompt` muss zwischen 1 und 6000 Zeichen lang sein. Die `source_generation_id` ist erforderlich und muss mit der `generation_id`-Ausgabe eines vorherigen Luma Ray 3.2-Nodes verbunden werden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das generierte 5-sekündige erweiterte Videosegment. | VIDEO |
| `generation_id` | Eindeutige Kennung für diese Generierung, die mit einem weiteren Luma Ray 3.2 Extend Video-Node für weitere Erweiterungen verbunden werden kann. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
